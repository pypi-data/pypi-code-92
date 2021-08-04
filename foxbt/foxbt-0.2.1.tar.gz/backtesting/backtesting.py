"""
Core framework data structures.
Objects from this module can also be imported from the top-level
module directly, e.g.

    from backtesting import Backtest, Strategy
"""
import multiprocessing as mp
import os
import sys
import warnings
from abc import abstractmethod, ABCMeta
from concurrent.futures import ProcessPoolExecutor, as_completed
from copy import copy
from functools import lru_cache, partial
from itertools import repeat, product, chain, compress
from math import copysign
from numbers import Number
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Type, Union

import numpy as np
import pandas as pd

try:
    from tqdm.auto import tqdm as _tqdm

    _tqdm = partial(_tqdm, leave=False)
except ImportError:

    def _tqdm(seq, **_):
        return seq


from ._plotting import plot
from ._util import _as_str, _Indicator, _Data, _data_period, try_


__pdoc__ = {
    "Strategy.__init__": False,
    "Order.__init__": False,
    "Position.__init__": False,
    "Trade.__init__": False,
}


class Strategy(metaclass=ABCMeta):
    """
    A trading strategy base class. Extend this class and
    override methods
    `backtesting.backtesting.Strategy.init` and
    `backtesting.backtesting.Strategy.next` to define
    your own strategy.
    """

    def __init__(self, broker, data, params):
        self._indicators = []
        self._broker: _Broker = broker
        self._data: _Data = data
        self._params = self._check_params(params)

    def __repr__(self):
        return "<Strategy " + str(self) + ">"

    def __str__(self):
        params = ",".join(
            f"{i[0]}={i[1]}"
            for i in zip(self._params.keys(), map(_as_str, self._params.values()))
        )
        if params:
            params = "(" + params + ")"
        return f"{self.__class__.__name__}{params}"

    def _check_params(self, params):
        for k, v in params.items():
            if not hasattr(self, k):
                raise AttributeError(
                    f"Strategy '{self.__class__.__name__}' is missing parameter '{k}'."
                    "Strategy class should define parameters as class variables before they "
                    "can be optimized or run with."
                )
            setattr(self, k, v)
        return params

    def update_params(self, params):
        self._params = self._check_params(params)

    def I(
        self,  # noqa: E741, E743
        func: Callable,
        *args,
        name=None,
        plot=True,
        overlay=None,
        color=None,
        scatter=False,
        **kwargs,
    ) -> np.ndarray:
        """
        Declare indicator. An indicator is just an array of values,
        but one that is revealed gradually in
        `backtesting.backtesting.Strategy.next` much like
        `backtesting.backtesting.Strategy.data` is.
        Returns `np.ndarray` of indicator values.

        `func` is a function that returns the indicator array(s) of
        same length as `backtesting.backtesting.Strategy.data`.

        In the plot legend, the indicator is labeled with
        function name, unless `name` overrides it.

        If `plot` is `True`, the indicator is plotted on the resulting
        `backtesting.backtesting.Backtest.plot`.

        If `overlay` is `True`, the indicator is plotted overlaying the
        price candlestick chart (suitable e.g. for moving averages).
        If `False`, the indicator is plotted standalone below the
        candlestick chart. By default, a heuristic is used which decides
        correctly most of the time.

        `color` can be string hex RGB triplet or X11 color name.
        By default, the next available color is assigned.

        If `scatter` is `True`, the plotted indicator marker will be a
        circle instead of a connected line segment (default).

        Additional `*args` and `**kwargs` are passed to `func` and can
        be used for parameters.

        For example, using simple moving average function from TA-Lib:

            def init():
                self.sma = self.I(ta.SMA, self.data.Close, self.n_sma)
        """
        if name is None:
            params = ",".join(filter(None, map(_as_str, chain(args, kwargs.values()))))
            func_name = _as_str(func)
            name = f"{func_name}({params})" if params else f"{func_name}"
        else:
            name = name.format(
                *map(_as_str, args),
                **dict(zip(kwargs.keys(), map(_as_str, kwargs.values()))),
            )

        try:
            value = func(*args, **kwargs)
        except Exception as e:
            raise RuntimeError(f'Indicator "{name}" errored with exception: {e}')

        if isinstance(value, pd.DataFrame):
            value = value.values.T

        if value is not None:
            value = try_(lambda: np.asarray(value, order="C"), None)
        is_arraylike = value is not None

        # Optionally flip the array if the user returned e.g. `df.values`
        if is_arraylike and np.argmax(value.shape) == 0:
            value = value.T

        if (
            not is_arraylike
            or not 1 <= value.ndim <= 2
            or value.shape[-1] != len(self._data.Close)
        ):
            raise ValueError(
                "Indicators must return (optionally a tuple of) numpy.arrays of same "
                f'length as `data` (data shape: {self._data.Close.shape}; indicator "{name}"'
                f'shape: {getattr(value, "shape" , "")}, returned value: {value})'
            )

        if plot and overlay is None and np.issubdtype(value.dtype, np.number):
            x = value / self._data.Close
            # By default, overlay if strong majority of indicator values
            # is within 30% of Close
            with np.errstate(invalid="ignore"):
                overlay = ((x < 1.4) & (x > 0.6)).mean() > 0.6

        value = _Indicator(
            value,
            name=name,
            plot=plot,
            overlay=overlay,
            color=color,
            scatter=scatter,
            # _Indicator.s Series accessor uses this:
            index=self.data.index,
        )
        self._indicators.append(value)
        return value

    @abstractmethod
    def init(self):
        """
        Initialize the strategy.
        Override this method.
        Declare indicators (with `backtesting.backtesting.Strategy.I`).
        Precompute what needs to be precomputed or can be precomputed
        in a vectorized fashion before the strategy starts.

        If you extend composable strategies from `backtesting.lib`,
        make sure to call:

            super().init()
        """

    @abstractmethod
    def next(self):
        """
        Main strategy runtime method, called as each new
        `backtesting.backtesting.Strategy.data`
        instance (row; full candlestick bar) becomes available.
        This is the main method where strategy decisions
        upon data precomputed in `backtesting.backtesting.Strategy.init`
        take place.

        If you extend composable strategies from `backtesting.lib`,
        make sure to call:

            super().next()
        """

    class __FULL_EQUITY(float):
        def __repr__(self):
            return ".9999"

    _FULL_EQUITY = __FULL_EQUITY(1 - sys.float_info.epsilon)

    def buy(
        self,
        *,
        size: float = _FULL_EQUITY,
        limit: float = None,
        stop: float = None,
        sl: float = None,
        tp: float = None,
    ):
        """
        Place a new long order. For explanation of parameters, see `Order` and its properties.

        See also `Strategy.sell()`.
        """
        assert (
            0 < size < 1 or round(size) == size
        ), "size must be a positive fraction of equity, or a positive whole number of units"
        return self._broker.new_order(size, limit, stop, sl, tp)

    def sell(
        self,
        *,
        size: float = _FULL_EQUITY,
        limit: float = None,
        stop: float = None,
        sl: float = None,
        tp: float = None,
    ):
        """
        Place a new short order. For explanation of parameters, see `Order` and its properties.

        See also `Strategy.buy()`.
        """
        assert (
            0 < size < 1 or round(size) == size
        ), "size must be a positive fraction of equity, or a positive whole number of units"
        return self._broker.new_order(-size, limit, stop, sl, tp)

    @property
    def equity(self) -> float:
        """Current account equity (cash plus assets)."""
        return self._broker.equity

    @property
    def data(self) -> _Data:
        """
        Price data, roughly as passed into
        `backtesting.backtesting.Backtest.__init__`,
        but with two significant exceptions:

        * `data` is _not_ a DataFrame, but a custom structure
          that serves customized numpy arrays for reasons of performance
          and convenience. Besides OHLCV columns, `.index` and length,
          it offers `.pip` property, the smallest price unit of change.
        * Within `backtesting.backtesting.Strategy.init`, `data` arrays
          are available in full length, as passed into
          `backtesting.backtesting.Backtest.__init__`
          (for precomputing indicators and such). However, within
          `backtesting.backtesting.Strategy.next`, `data` arrays are
          only as long as the current iteration, simulating gradual
          price point revelation. In each call of
          `backtesting.backtesting.Strategy.next` (iteratively called by
          `backtesting.backtesting.Backtest` internally),
          the last array value (e.g. `data.Close[-1]`)
          is always the _most recent_ value.
        * If you need data arrays (e.g. `data.Close`) to be indexed
          **Pandas series**, you can call their `.s` accessor
          (e.g. `data.Close.s`). If you need the whole of data
          as a **DataFrame**, use `.df` accessor (i.e. `data.df`).
        """
        return self._data

    @property
    def position(self) -> "Position":
        """Instance of `backtesting.backtesting.Position`."""
        return self._broker.position

    @property
    def orders(self) -> "Tuple[Order, ...]":
        """List of orders (see `Order`) waiting for execution."""
        return _Orders(self._broker.orders)

    @property
    def trades(self) -> "Tuple[Trade, ...]":
        """List of active trades (see `Trade`)."""
        return tuple(self._broker.trades)

    @property
    def closed_trades(self) -> "Tuple[Trade, ...]":
        """List of settled trades (see `Trade`)."""
        return tuple(self._broker.closed_trades)


class _Orders(tuple):
    """
    TODO: remove this class. Only for deprecation.
    """

    def cancel(self):
        """Cancel all non-contingent (i.e. SL/TP) orders."""
        for order in self:
            if not order.is_contingent:
                order.cancel()

    def __getattr__(self, item):
        # TODO: Warn on deprecations from the previous version. Remove in the next.
        removed_attrs = (
            "entry",
            "set_entry",
            "is_long",
            "is_short",
            "sl",
            "tp",
            "set_sl",
            "set_tp",
        )
        if item in removed_attrs:
            raise AttributeError(
                f'Strategy.orders.{"/.".join(removed_attrs)} were removed in'
                "Backtesting 0.2.0. "
                "Use `Order` API instead. See docs."
            )
        raise AttributeError(f"'tuple' object has no attribute {item!r}")


class Position:
    """
    Currently held asset position, available as
    `backtesting.backtesting.Strategy.position` within
    `backtesting.backtesting.Strategy.next`.
    Can be used in boolean contexts, e.g.

        if self.position:
            ...  # we have a position, either long or short
    """

    def __init__(self, broker: "_Broker"):
        self.__broker = broker

    def __bool__(self):
        return self.size != 0

    @property
    def size(self) -> float:
        """Position size in units of asset. Negative if position is short."""
        return sum(trade.size for trade in self.__broker.trades)

    @property
    def pl(self) -> float:
        """Profit (positive) or loss (negative) of the current position in cash units."""
        return sum(trade.pl for trade in self.__broker.trades)

    @property
    def pl_pct(self) -> float:
        """Profit (positive) or loss (negative) of the current position in percent."""
        weights = np.abs([trade.size for trade in self.__broker.trades])
        weights = weights / weights.sum()
        pl_pcts = np.array([trade.pl_pct for trade in self.__broker.trades])
        return (pl_pcts * weights).sum()

    @property
    def is_long(self) -> bool:
        """True if the position is long (position size is positive)."""
        return self.size > 0

    @property
    def is_short(self) -> bool:
        """True if the position is short (position size is negative)."""
        return self.size < 0

    def close(self, portion: float = 1.0):
        """
        Close portion of position by closing `portion` of each active trade. See `Trade.close`.
        """
        for trade in self.__broker.trades:
            trade.close(portion)

    def __repr__(self):
        return f"<Position: {self.size} ({len(self.__broker.trades)} trades)>"


class _OutOfMoneyError(Exception):
    pass


class Order:
    """
    Place new orders through `Strategy.buy()` and `Strategy.sell()`.
    Query existing orders through `Strategy.orders`.

    When an order is executed or [filled], it results in a `Trade`.

    If you wish to modify aspects of a placed but not yet filled order,
    cancel it and place a new one instead.

    All placed orders are [Good 'Til Canceled].

    [filled]: https://www.investopedia.com/terms/f/fill.asp
    [Good 'Til Canceled]: https://www.investopedia.com/terms/g/gtc.asp
    """

    def __init__(
        self,
        broker: "_Broker",
        size: float,
        limit_price: float = None,
        stop_price: float = None,
        sl_price: float = None,
        tp_price: float = None,
        parent_trade: "Trade" = None,
    ):
        self.__broker = broker
        assert size != 0
        self.__size = size
        self.__limit_price = limit_price
        self.__stop_price = stop_price
        self.__sl_price = sl_price
        self.__tp_price = tp_price
        self.__parent_trade = parent_trade

    def _replace(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, f"_{self.__class__.__qualname__}__{k}", v)
        return self

    def __repr__(self):
        return "<Order {}>".format(
            ", ".join(
                f"{param}={round(value, 5)}"
                for param, value in (
                    ("size", self.__size),
                    ("limit", self.__limit_price),
                    ("stop", self.__stop_price),
                    ("sl", self.__sl_price),
                    ("tp", self.__tp_price),
                    ("contingent", self.is_contingent),
                )
                if value is not None
            )
        )

    def cancel(self):
        """Cancel the order."""
        self.__broker.orders.remove(self)
        trade = self.__parent_trade
        if trade:
            if self is trade._sl_order:
                trade._replace(sl_order=None)
            elif self is trade._tp_order:
                trade._replace(tp_order=None)
            else:
                assert False

    # Fields getters

    @property
    def size(self) -> float:
        """
        Order size (negative for short orders).

        If size is a value between 0 and 1, it is interpreted as a fraction of current
        available liquidity (cash plus `Position.pl` minus used margin).
        A value greater than or equal to 1 indicates an absolute number of units.
        """
        return self.__size

    @property
    def limit(self) -> Optional[float]:
        """
        Order limit price for [limit orders], or None for [market orders],
        which are filled at next available price.

        [limit orders]: https://www.investopedia.com/terms/l/limitorder.asp
        [market orders]: https://www.investopedia.com/terms/m/marketorder.asp
        """
        return self.__limit_price

    @property
    def stop(self) -> Optional[float]:
        """
        Order stop price for [stop-limit/stop-market][_] order,
        otherwise None if no stop was set, or the stop price has already been hit.

        [_]: https://www.investopedia.com/terms/s/stoporder.asp
        """
        return self.__stop_price

    @property
    def sl(self) -> Optional[float]:
        """
        A stop-loss price at which, if set, a new contingent stop-market order
        will be placed upon the `Trade` following this order's execution.
        See also `Trade.sl`.
        """
        return self.__sl_price

    @property
    def tp(self) -> Optional[float]:
        """
        A take-profit price at which, if set, a new contingent limit order
        will be placed upon the `Trade` following this order's execution.
        See also `Trade.tp`.
        """
        return self.__tp_price

    @property
    def parent_trade(self):
        return self.__parent_trade

    __pdoc__["Order.parent_trade"] = False

    # Extra properties

    @property
    def is_long(self):
        """True if the order is long (order size is positive)."""
        return self.__size > 0

    @property
    def is_short(self):
        """True if the order is short (order size is negative)."""
        return self.__size < 0

    @property
    def is_contingent(self):
        """
        True for [contingent] orders, i.e. [OCO] stop-loss and take-profit bracket orders
        placed upon an active trade. Remaining contingent orders are canceled when
        their parent `Trade` is closed.

        You can modify contingent orders through `Trade.sl` and `Trade.tp`.

        [contingent]: https://www.investopedia.com/terms/c/contingentorder.asp
        [OCO]: https://www.investopedia.com/terms/o/oco.asp
        """
        return bool(self.__parent_trade)


class Trade:
    """
    When an `Order` is filled, it results in an active `Trade`.
    Find active trades in `Strategy.trades` and closed, settled trades in `Strategy.closed_trades`.
    """

    def __init__(self, broker: "_Broker", size: int, entry_price: float, entry_bar):
        self.__broker = broker
        self.__size = size
        self.__entry_price = entry_price
        self.__exit_price: Optional[float] = None
        self.__entry_bar: int = entry_bar
        self.__exit_bar: Optional[int] = None
        self.__sl_order: Optional[Order] = None
        self.__tp_order: Optional[Order] = None

    def __repr__(self):
        return (
            f'<Trade size={self.__size} time={self.__entry_bar}-{self.__exit_bar or ""} '
            f'price={self.__entry_price}-{self.__exit_price or ""} pl={self.pl:.0f}>'
        )

    def _replace(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, f"_{self.__class__.__qualname__}__{k}", v)
        return self

    def _copy(self, **kwargs):
        return copy(self)._replace(**kwargs)

    def close(self, portion: float = 1.0):
        """Place new `Order` to close `portion` of the trade at next market price."""
        assert 0 < portion <= 1, "portion must be a fraction between 0 and 1"
        size = copysign(max(1, round(abs(self.__size) * portion)), -self.__size)
        order = Order(self.__broker, size, parent_trade=self)
        self.__broker.orders.insert(0, order)

    # Fields getters

    @property
    def size(self):
        """Trade size (volume; negative for short trades)."""
        return self.__size

    @property
    def entry_price(self) -> float:
        """Trade entry price."""
        return self.__entry_price

    @property
    def exit_price(self) -> Optional[float]:
        """Trade exit price (or None if the trade is still active)."""
        return self.__exit_price

    @property
    def entry_bar(self) -> int:
        """Candlestick bar index of when the trade was entered."""
        return self.__entry_bar

    @property
    def exit_bar(self) -> Optional[int]:
        """
        Candlestick bar index of when the trade was exited
        (or None if the trade is still active).
        """
        return self.__exit_bar

    @property
    def _sl_order(self):
        return self.__sl_order

    @property
    def _tp_order(self):
        return self.__tp_order

    # Extra properties

    @property
    def entry_time(self) -> Union[pd.Timestamp, int]:
        """Datetime of when the trade was entered."""
        return self.__broker._data.index[self.__entry_bar]

    @property
    def exit_time(self) -> Optional[Union[pd.Timestamp, int]]:
        """Datetime of when the trade was exited."""
        if self.__exit_bar is None:
            return None
        return self.__broker._data.index[self.__exit_bar]

    @property
    def is_long(self):
        """True if the trade is long (trade size is positive)."""
        return self.__size > 0

    @property
    def is_short(self):
        """True if the trade is short (trade size is negative)."""
        return not self.is_long

    @property
    def pl(self):
        """Trade profit (positive) or loss (negative) in cash units."""
        price = self.__exit_price or self.__broker.last_price
        return self.__size * (price - self.__entry_price)

    @property
    def pl_pct(self):
        """Trade profit (positive) or loss (negative) in percent."""
        price = self.__exit_price or self.__broker.last_price
        return copysign(1, self.__size) * (price / self.__entry_price - 1)

    @property
    def value(self):
        """Trade total value in cash (volume × price)."""
        price = self.__exit_price or self.__broker.last_price
        return abs(self.__size) * price

    # SL/TP management API

    @property
    def sl(self):
        """
        Stop-loss price at which to close the trade.

        This variable is writable. By assigning it a new price value,
        you create or modify the existing SL order.
        By assigning it `None`, you cancel it.
        """
        return self.__sl_order and self.__sl_order.stop

    @sl.setter
    def sl(self, price: float):
        self.__set_contingent("sl", price)

    @property
    def tp(self):
        """
        Take-profit price at which to close the trade.

        This property is writable. By assigning it a new price value,
        you create or modify the existing TP order.
        By assigning it `None`, you cancel it.
        """
        return self.__tp_order and self.__tp_order.limit

    @tp.setter
    def tp(self, price: float):
        self.__set_contingent("tp", price)

    def __set_contingent(self, type, price):
        assert type in ("sl", "tp")
        assert price is None or 0 < price < np.inf
        attr = f"_{self.__class__.__qualname__}__{type}_order"
        order: Order = getattr(self, attr)
        if order:
            order.cancel()
        if price:
            kwargs = dict(stop=price) if type == "sl" else dict(limit=price)
            order = self.__broker.new_order(-self.size, trade=self, **kwargs)
            setattr(self, attr, order)


class _Broker:
    def __init__(
        self,
        *,
        data,
        cash,
        commission,
        margin,
        trade_on_close,
        hedging,
        exclusive_orders,
        index,
    ):
        assert 0 < cash, f"cash should be >0, is {cash}"
        assert -0.1 <= commission < 0.1, (
            "commission should be between -10% "
            f"(e.g. market-maker's rebates) and 10% (fees), is {commission}"
        )
        assert 0 < margin <= 1, f"margin should be between 0 and 1, is {margin}"
        self._data: _Data = data
        self._cash = cash
        self._commission = commission
        self._leverage = 1 / margin
        self._trade_on_close = trade_on_close
        self._hedging = hedging
        self._exclusive_orders = exclusive_orders

        self._equity = np.tile(np.nan, len(index))
        self.orders: List[Order] = []
        self.trades: List[Trade] = []
        self.position = Position(self)
        self.closed_trades: List[Trade] = []

    def __repr__(self):
        return f"<Broker: {self._cash:.0f}{self.position.pl:+.1f} ({len(self.trades)} trades)>"

    def new_order(
        self,
        size: float,
        limit: float = None,
        stop: float = None,
        sl: float = None,
        tp: float = None,
        *,
        trade: Trade = None,
    ):
        """
        Argument size indicates whether the order is long or short
        """
        size = float(size)
        stop = stop and float(stop)
        limit = limit and float(limit)
        sl = sl and float(sl)
        tp = tp and float(tp)

        is_long = size > 0
        adjusted_price = self._adjusted_price(size)

        if is_long:
            if not (sl or -np.inf) < (limit or stop or adjusted_price) < (tp or np.inf):
                raise ValueError(
                    "Long orders require: "
                    f"SL ({sl}) < LIMIT ({limit or stop or adjusted_price}) < TP ({tp})"
                )
        else:
            if not (tp or -np.inf) < (limit or stop or adjusted_price) < (sl or np.inf):
                raise ValueError(
                    "Short orders require: "
                    f"TP ({tp}) < LIMIT ({limit or stop or adjusted_price}) < SL ({sl})"
                )

        order = Order(self, size, limit, stop, sl, tp, trade)
        # Put the new order in the order queue,
        # inserting SL/TP/trade-closing orders in-front
        if trade:
            self.orders.insert(0, order)
        else:
            # If exclusive orders (each new order auto-closes previous orders/position),
            # cancel all non-contingent orders and close all open trades beforehand
            if self._exclusive_orders:
                for o in self.orders:
                    if not o.is_contingent:
                        o.cancel()
                for t in self.trades:
                    t.close()

            self.orders.append(order)

        return order

    @property
    def last_price(self) -> float:
        """ Price at the last (current) close. """
        return self._data.Close[-1]

    def _adjusted_price(self, size=None, price=None) -> float:
        """
        Long/short `price`, adjusted for commisions.
        In long positions, the adjusted price is a fraction higher, and vice versa.
        """
        return (price or self.last_price) * (1 + copysign(self._commission, size))

    @property
    def equity(self) -> float:
        return self._cash + sum(trade.pl for trade in self.trades)

    @property
    def margin_available(self) -> float:
        # From https://github.com/QuantConnect/Lean/pull/3768
        margin_used = sum(trade.value / self._leverage for trade in self.trades)
        return max(0, self.equity - margin_used)

    def next(self):
        i = self._i = len(self._data) - 1
        self._process_orders()

        # Log account equity for the equity curve
        equity = self.equity
        self._equity[i] = equity

        # If equity is negative, set all to 0 and stop the simulation
        if equity <= 0:
            assert self.margin_available <= 0
            for trade in self.trades:
                self._close_trade(trade, self._data.Close[-1], i)
            self._cash = 0
            self._equity[i:] = 0
            raise _OutOfMoneyError

    def _process_orders(self):
        data = self._data
        open, high, low = data.Open[-1], data.High[-1], data.Low[-1]
        prev_close = data.Close[-2]
        reprocess_orders = False

        # Process orders
        for order in list(self.orders):  # type: Order

            # Related SL/TP order was already removed
            if order not in self.orders:
                continue

            # Check if stop condition was hit
            stop_price = order.stop
            if stop_price:
                is_stop_hit = (
                    (high > stop_price) if order.is_long else (low < stop_price)
                )
                if not is_stop_hit:
                    continue

                # > When the stop price is reached, a stop order becomes a market/limit order.
                # https://www.sec.gov/fast-answers/answersstopordhtm.html
                order._replace(stop_price=None)

            # Determine purchase price.
            # Check if limit order can be filled.
            if order.limit:
                is_limit_hit = (
                    low < order.limit if order.is_long else high > order.limit
                )
                # When stop and limit are hit within the same bar, we pessimistically
                # assume limit was hit before the stop (i.e. "before it counts")
                is_limit_hit_before_stop = is_limit_hit and (
                    order.limit < (stop_price or -np.inf)
                    if order.is_long
                    else order.limit > (stop_price or np.inf)
                )
                if not is_limit_hit or is_limit_hit_before_stop:
                    continue

                # stop_price, if set, was hit within this bar
                price = (
                    min(stop_price or open, order.limit)
                    if order.is_long
                    else max(stop_price or open, order.limit)
                )
            else:
                # Market-if-touched / market order
                price = prev_close if self._trade_on_close else open
                price = (
                    max(price, stop_price or -np.inf)
                    if order.is_long
                    else min(price, stop_price or np.inf)
                )

            # Determine entry/exit bar index
            is_market_order = not order.limit and not stop_price
            time_index = (
                (self._i - 1) if is_market_order and self._trade_on_close else self._i
            )

            # If order is a SL/TP order, it should close an existing trade it was contingent upon
            if order.parent_trade:
                trade = order.parent_trade
                _prev_size = trade.size
                # If order.size is "greater" than trade.size, this order is a trade.close()
                # order and part of the trade was already closed beforehand
                size = copysign(min(abs(_prev_size), abs(order.size)), order.size)
                # If this trade isn't already closed (e.g. on multiple `trade.close(.5)` calls)
                if trade in self.trades:
                    self._reduce_trade(trade, price, size, time_index)
                    assert order.size != -_prev_size or trade not in self.trades
                if order in (trade._sl_order, trade._tp_order):
                    assert order.size == -trade.size
                    assert order not in self.orders  # Removed when trade was closed
                else:
                    # It's a trade.close() order, now done
                    assert abs(_prev_size) >= abs(size) >= 1
                    self.orders.remove(order)
                continue

            # Else this is a stand-alone trade

            # Adjust price to include commission (or bid-ask spread).
            # In long positions, the adjusted price is a fraction higher, and vice versa.
            adjusted_price = self._adjusted_price(order.size, price)

            # If order size was specified proportionally,
            # precompute true size in units, accounting for margin and spread/commissions
            size = order.size
            if -1 < size < 1:
                size = copysign(
                    int(
                        (self.margin_available * self._leverage * abs(size))
                        // adjusted_price
                    ),
                    size,
                )
                # Not enough cash/margin even for a single unit
                if not size:
                    self.orders.remove(order)
                    continue
            assert size == round(size)
            need_size = int(size)

            if not self._hedging:
                # Fill position by FIFO closing/reducing existing opposite-facing trades.
                # Existing trades are closed at unadjusted price, because the adjustment
                # was already made when buying.
                for trade in list(self.trades):
                    if trade.is_long == order.is_long:
                        continue
                    assert trade.size * order.size < 0

                    # Order size greater than this opposite-directed existing trade,
                    # so it will be closed completely
                    if abs(need_size) >= abs(trade.size):
                        self._close_trade(trade, price, time_index)
                        need_size += trade.size
                    else:
                        # The existing trade is larger than the new order,
                        # so it will only be closed partially
                        self._reduce_trade(trade, price, need_size, time_index)
                        need_size = 0

                    if not need_size:
                        break

            # If we don't have enough liquidity to cover for the order, cancel it
            if abs(need_size) * adjusted_price > self.margin_available * self._leverage:
                self.orders.remove(order)
                continue

            # Open a new trade
            if need_size:
                self._open_trade(
                    adjusted_price, need_size, order.sl, order.tp, time_index
                )

                # We need to reprocess the SL/TP orders newly added to the queue.
                # This allows e.g. SL hitting in the same bar the order was open.
                # See https://github.com/kernc/backtesting.py/issues/119
                if order.sl or order.tp:
                    if is_market_order:
                        reprocess_orders = True
                    elif (
                        low <= (order.sl or -np.inf) <= high
                        or low <= (order.tp or -np.inf) <= high
                    ):
                        warnings.warn(
                            f"({data.index[-1]}) A contingent SL/TP order would execute in the "
                            "same bar its parent stop/limit order was turned into a trade. "
                            "Since we can't assert the precise intra-candle "
                            "price movement, the affected SL/TP order will instead be executed on "
                            "the next (matching) price/bar, making the result (of this trade) "
                            "somewhat dubious. "
                            "See https://github.com/kernc/backtesting.py/issues/119",
                            UserWarning,
                        )

            # Order processed
            self.orders.remove(order)

        if reprocess_orders:
            self._process_orders()

    def _reduce_trade(self, trade: Trade, price: float, size: float, time_index: int):
        assert trade.size * size < 0
        assert abs(trade.size) >= abs(size)

        size_left = trade.size + size
        assert size_left * trade.size >= 0
        if not size_left:
            close_trade = trade
        else:
            # Reduce existing trade ...
            trade._replace(size=size_left)
            if trade._sl_order:
                trade._sl_order._replace(size=-trade.size)
            if trade._tp_order:
                trade._tp_order._replace(size=-trade.size)

            # ... by closing a reduced copy of it
            close_trade = trade._copy(size=-size, sl_order=None, tp_order=None)
            self.trades.append(close_trade)

        self._close_trade(close_trade, price, time_index)

    def _close_trade(self, trade: Trade, price: float, time_index: int):
        self.trades.remove(trade)
        if trade._sl_order:
            self.orders.remove(trade._sl_order)
        if trade._tp_order:
            self.orders.remove(trade._tp_order)

        self.closed_trades.append(trade._replace(exit_price=price, exit_bar=time_index))
        self._cash += trade.pl

    def _open_trade(
        self, price: float, size: int, sl: float, tp: float, time_index: int
    ):
        trade = Trade(self, size, price, time_index)
        self.trades.append(trade)
        # Create SL/TP (bracket) orders.
        # Make sure SL order is created first so it gets adversarially processed before TP order
        # in case of an ambiguous tie (both hit within a single bar).
        # Note, sl/tp orders are inserted at the front of the list, thus order reversed.
        if tp:
            trade.tp = tp
        if sl:
            trade.sl = sl


class Backtest:
    """
    Backtest a particular (parameterized) strategy
    on particular data.

    Upon initialization, call method
    `backtesting.backtesting.Backtest.run` to run a backtest
    instance, or `backtesting.backtesting.Backtest.optimize` to
    optimize it.
    """

    def __init__(
        self,
        data: pd.DataFrame,
        strategy: Type[Strategy],
        *,
        cash: float = 10_000,
        commission: float = 0.0,
        margin: float = 1.0,
        trade_on_close=False,
        hedging=False,
        exclusive_orders=False,
    ):
        """
        Initialize a backtest. Requires data and a strategy to test.

        `data` is a `pd.DataFrame` with columns:
        `Open`, `High`, `Low`, `Close`, and (optionally) `Volume`.
        If any columns are missing, set them to what you have available,
        e.g.

            df['Open'] = df['High'] = df['Low'] = df['Close']

        The passed data frame can contain additional columns that
        can be used by the strategy (e.g. sentiment info).
        DataFrame index can be either a datetime index (timestamps)
        or a monotonic range index (i.e. a sequence of periods).

        `strategy` is a `backtesting.backtesting.Strategy`
        _subclass_ (not an instance).

        `cash` is the initial cash to start with.

        `commission` is the commission ratio. E.g. if your broker's commission
        is 1% of trade value, set commission to `0.01`. Note, if you wish to
        account for bid-ask spread, you can approximate doing so by increasing
        the commission, e.g. set it to `0.0002` for commission-less forex
        trading where the average spread is roughly 0.2‰ of asking price.

        `margin` is the required margin (ratio) of a leveraged account.
        No difference is made between initial and maintenance margins.
        To run the backtest using e.g. 50:1 leverge that your broker allows,
        set margin to `0.02` (1 / leverage).

        If `trade_on_close` is `True`, market orders will be filled
        with respect to the current bar's closing price instead of the
        next bar's open.

        If `hedging` is `True`, allow trades in both directions simultaneously.
        If `False`, the opposite-facing orders first close existing trades in
        a [FIFO] manner.

        If `exclusive_orders` is `True`, each new order auto-closes the previous
        trade/position, making at most a single trade (long or short) in effect
        at each time.

        [FIFO]: https://www.investopedia.com/terms/n/nfa-compliance-rule-2-43b.asp
        """

        if not (isinstance(strategy, type) and issubclass(strategy, Strategy)):
            raise TypeError("`strategy` must be a Strategy sub-type")
        if not isinstance(data, pd.DataFrame):
            raise TypeError("`data` must be a pandas.DataFrame with columns")
        if not isinstance(commission, Number):
            raise TypeError(
                "`commission` must be a float value, percent of " "entry order price"
            )

        data = data.copy(deep=False)

        # Convert index to datetime index
        if (
            not isinstance(data.index, pd.DatetimeIndex)
            and not isinstance(data.index, pd.RangeIndex)
            and
            # Numeric index with most large numbers
            (
                data.index.is_numeric()
                and (data.index > pd.Timestamp("1975").timestamp()).mean() > 0.8
            )
        ):
            try:
                data.index = pd.to_datetime(data.index, infer_datetime_format=True)
            except ValueError:
                pass

        if "Volume" not in data:
            data["Volume"] = np.nan

        if len(data) == 0:
            raise ValueError("OHLC `data` is empty")
        if (
            len(data.columns.intersection({"Open", "High", "Low", "Close", "Volume"}))
            != 5
        ):
            raise ValueError(
                "`data` must be a pandas.DataFrame with columns "
                "'Open', 'High', 'Low', 'Close', and (optionally) 'Volume'"
            )
        if data[["Open", "High", "Low", "Close"]].isnull().values.any():
            raise ValueError(
                "Some OHLC values are missing (NaN). "
                "Please strip those lines with `df.dropna()` or "
                "fill them in with `df.interpolate()` or whatever."
            )
        if np.any(data["Close"] > cash):
            warnings.warn(
                "Some prices are larger than initial cash value. Note that fractional "
                "trading is not supported. If you want to trade Bitcoin, "
                "increase initial cash, or trade μBTC or satoshis instead (GH-134).",
                stacklevel=2,
            )
        if not data.index.is_monotonic_increasing:
            warnings.warn(
                "Data index is not sorted in ascending order. Sorting.", stacklevel=2
            )
            data = data.sort_index()
        if not isinstance(data.index, pd.DatetimeIndex):
            warnings.warn(
                "Data index is not datetime. Assuming simple periods, "
                "but `pd.DateTimeIndex` is advised.",
                stacklevel=2,
            )

        self._data: pd.DataFrame = data
        self._broker = partial(
            _Broker,
            cash=cash,
            commission=commission,
            margin=margin,
            trade_on_close=trade_on_close,
            hedging=hedging,
            exclusive_orders=exclusive_orders,
            index=data.index,
        )
        self._strategy = strategy
        self._results = None

    def run(self, **kwargs) -> pd.Series:
        """
        Run the backtest. Returns `pd.Series` with results and statistics.

        Keyword arguments are interpreted as strategy parameters.

            >>> Backtest(GOOG, SmaCross).run()
            Start                     2004-08-19 00:00:00
            End                       2013-03-01 00:00:00
            Duration                   3116 days 00:00:00
            Exposure Time [%]                     93.9944
            Equity Final [$]                      51959.9
            Equity Peak [$]                       75787.4
            Return [%]                            419.599
            Buy & Hold Return [%]                 703.458
            Return (Ann.) [%]                      21.328
            Volatility (Ann.) [%]                 36.5383
            Sharpe Ratio                         0.583718
            Sortino Ratio                         1.09239
            Calmar Ratio                         0.444518
            Max. Drawdown [%]                    -47.9801
            Avg. Drawdown [%]                    -5.92585
            Max. Drawdown Duration      584 days 00:00:00
            Avg. Drawdown Duration       41 days 00:00:00
            # Trades                                   65
            Win Rate [%]                          46.1538
            Best Trade [%]                         53.596
            Worst Trade [%]                      -18.3989
            Avg. Trade [%]                        2.35371
            Max. Trade Duration         183 days 00:00:00
            Avg. Trade Duration          46 days 00:00:00
            Profit Factor                         2.08802
            Expectancy [%]                        8.79171
            SQN                                  0.916893
            _strategy                            SmaCross
            _equity_curve                           Eq...
            _trades                       Size  EntryB...
            dtype: object
        """
        data = _Data(self._data.copy(deep=False))
        broker: _Broker = self._broker(data=data)
        strategy: Strategy = self._strategy(broker, data, kwargs)

        strategy.init()
        data._update()  # Strategy.init might have changed/added to data.df

        # Indicators used in Strategy.next()
        indicator_attrs = {
            attr: indicator
            for attr, indicator in strategy.__dict__.items()
            if isinstance(indicator, _Indicator)
        }.items()

        # Skip first few candles where indicators are still "warming up"
        # +1 to have at least two entries available
        start = 1 + max(
            (
                np.isnan(indicator.astype(float)).argmin(axis=-1).max()
                for _, indicator in indicator_attrs
            ),
            default=0,
        )

        # Disable "invalid value encountered in ..." warnings. Comparison
        # np.nan >= 3 is not invalid; it's False.
        with np.errstate(invalid="ignore"):

            for i in range(start, len(self._data)):
                # Prepare data and indicators for `next` call
                data._set_length(i + 1)
                for attr, indicator in indicator_attrs:
                    # Slice indicator on the last dimension (case of 2d indicator)
                    setattr(strategy, attr, indicator[..., : i + 1])

                # Handle orders processing and broker stuff
                try:
                    broker.next()
                except _OutOfMoneyError:
                    break

                # Next tick, a moment before bar close
                strategy.next()
            else:
                # Close any remaining open trades so they produce some stats
                for trade in broker.trades:
                    trade.close()

                # Re-run broker one last time to handle orders placed in the last strategy
                # iteration. Use the same OHLC values as in the last broker iteration.
                if start < len(self._data):
                    try_(broker.next, exception=_OutOfMoneyError)

            # Set data back to full length
            # for future `indicator._opts['data'].index` calls to work
            data._set_length(len(self._data))

            self._results = self._compute_stats(broker, strategy)
        return self._results

    def validation_optimization(
        self,
        *,
        maximize: Union[str, Callable[[pd.Series], float]] = "SQN",
        method: str = "grid",
        max_tries: Union[int, float] = None,
        constraint: Callable[[dict], bool] = None,
        validation_portion: float = 0.3,
        **kwargs,
    ) -> Union[
        pd.Series, Tuple[pd.Series, pd.Series], Tuple[pd.Series, pd.Series, dict]
    ]:
        # In Sample
        [insample_optimization, optimizationParams] = self.optimize(
            maximize=maximize,
            method=method,
            max_tries=max_tries,
            constraint=constraint,
            start_data_portion=0,
            end_data_portion=1 - validation_portion,
            **kwargs,
        )

        # Out Sample
        datacopy = self._data.copy(deep=True)
        self._data = self._data[int(len(self._data) * (1 - validation_portion)) :]
        outsample_run = self.run(**optimizationParams)

        # Restore Data
        self._data = datacopy

        # Correlation
        outSampleLen = len(outsample_run["_equity_curve"])
        samples_corr = np.corrcoef(
            outsample_run["_equity_curve"]["Equity"],
            insample_optimization[0]["_equity_curve"]["Equity"][-outSampleLen:],
        )[1, 0]

        return insample_optimization, outsample_run, samples_corr

    # Walk-Forward Optimization
    def walk_forward_optimization(
        self,
        *,
        maximize: Union[str, Callable[[pd.Series], float]] = "SQN",
        method: str = "grid",
        max_tries: Union[int, float] = None,
        constraint: Callable[[dict], bool] = None,
        **kwargs,
    ) -> Union[
        pd.Series, Tuple[pd.Series, pd.Series], Tuple[pd.Series, pd.Series, dict]
    ]:
        data = _Data(self._data.copy(deep=False))
        broker: _Broker = self._broker(data=data)
        strategy: Strategy = self._strategy(broker, data, dict([]))

        strategy.init()
        data._update()  # Strategy.init might have changed/added to data.df

        # Indicators used in Strategy.next()
        indicator_attrs = {
            attr: indicator
            for attr, indicator in strategy.__dict__.items()
            if isinstance(indicator, _Indicator)
        }.items()

        # Skip first few candles where indicators are still "warming up"
        # skip to initial out sample portion of data
        # +1 to have at least two entries available
        start = 1 + max(
            max(
                (
                    np.isnan(indicator.astype(float)).argmin(axis=-1).max()
                    for _, indicator in indicator_attrs
                ),
                default=0,
            ),
            int(len(self._data) * 0.3) - 1,
        )

        # Disable "invalid value encountered in ..." warnings. Comparison
        # np.nan >= 3 is not invalid; it's False.
        with np.errstate(invalid="ignore"):
            splits = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            for i in range(start, len(self._data)):
                for s in splits:
                    if int(s * len(self._data)) == i:
                        Optimize = self.optimize(
                            maximize=maximize,
                            method=method,
                            max_tries=max_tries,
                            constraint=constraint,
                            start_data_portion=s - (0.3),
                            end_data_portion=s,
                            **kwargs,
                        )
                        strategy.update_params(Optimize[1])
                        strategy.init()

                # Prepare data and indicators for `next` call
                data._set_length(i + 1)
                for attr, indicator in indicator_attrs:
                    # Slice indicator on the last dimension (case of 2d indicator)
                    setattr(strategy, attr, indicator[..., : i + 1])

                # Handle orders processing and broker stuff
                try:
                    broker.next()
                except _OutOfMoneyError:
                    break

                # Next tick, a moment before bar close
                strategy.next()
            else:
                # Close any remaining open trades so they produce some stats
                for trade in broker.trades:
                    trade.close()

                # Re-run broker one last time to handle orders placed in the last strategy
                # iteration. Use the same OHLC values as in the last broker iteration.
                if start < len(self._data):
                    try_(broker.next, exception=_OutOfMoneyError)

            # Set data back to full length
            # for future `indicator._opts['data'].index` calls to work
            data._set_length(len(self._data))

            # Final Optimization
            FinalOptimize = self.optimize(
                maximize=maximize,
                method=method,
                max_tries=max_tries,
                constraint=constraint,
                start_data_portion=1 - (0.3),
                end_data_portion=1,
                **kwargs,
            )

            self._results = self._compute_stats(broker, strategy)
        return (self._results, FinalOptimize[1])

    # Cross-Validation Optimization
    def cross_validation_optimization(
        self,
        *,
        maximize: Union[str, Callable[[pd.Series], float]] = "SQN",
        method: str = "grid",
        max_tries: Union[int, float] = None,
        constraint: Callable[[dict], bool] = None,
        **kwargs,
    ) -> Union[
        pd.Series, Tuple[pd.Series, pd.Series], Tuple[pd.Series, pd.Series, dict]
    ]:
        data = _Data(self._data.copy(deep=False))
        broker: _Broker = self._broker(data=data)
        strategy: Strategy = self._strategy(broker, data, dict([]))

        strategy.init()
        data._update()  # Strategy.init might have changed/added to data.df

        # Indicators used in Strategy.next()
        indicator_attrs = {
            attr: indicator
            for attr, indicator in strategy.__dict__.items()
            if isinstance(indicator, _Indicator)
        }.items()

        # Skip first few candles where indicators are still "warming up"
        # skip to initial out sample portion of data
        # +1 to have at least two entries available
        start = 1 + max(
            max(
                (
                    np.isnan(indicator.astype(float)).argmin(axis=-1).max()
                    for _, indicator in indicator_attrs
                ),
                default=0,
            ),
            int(len(self._data) * 0.1) - 1,
        )

        # Disable "invalid value encountered in ..." warnings. Comparison
        # np.nan >= 3 is not invalid; it's False.
        with np.errstate(invalid="ignore"):
            splits = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            for i in range(start, len(self._data)):
                for s in splits:
                    if int(s * len(self._data)) == i:
                        Optimize = self.optimize(
                            maximize=maximize,
                            method=method,
                            max_tries=max_tries,
                            constraint=constraint,
                            start_data_portion=0,
                            end_data_portion=s,
                            **kwargs,
                        )
                        strategy.update_params(Optimize[1])
                        strategy.init()

                # Prepare data and indicators for `next` call
                data._set_length(i + 1)
                for attr, indicator in indicator_attrs:
                    # Slice indicator on the last dimension (case of 2d indicator)
                    setattr(strategy, attr, indicator[..., : i + 1])

                # Handle orders processing and broker stuff
                try:
                    broker.next()
                except _OutOfMoneyError:
                    break

                # Next tick, a moment before bar close
                strategy.next()
            else:
                # Close any remaining open trades so they produce some stats
                for trade in broker.trades:
                    trade.close()

                # Re-run broker one last time to handle orders placed in the last strategy
                # iteration. Use the same OHLC values as in the last broker iteration.
                if start < len(self._data):
                    try_(broker.next, exception=_OutOfMoneyError)

            # Set data back to full length
            # for future `indicator._opts['data'].index` calls to work
            data._set_length(len(self._data))

            # Final Optimization
            FinalOptimize = self.optimize(
                maximize=maximize,
                method=method,
                max_tries=max_tries,
                constraint=constraint,
                start_data_portion=0,
                end_data_portion=1,
                **kwargs,
            )

            self._results = self._compute_stats(broker, strategy)
        return (self._results, FinalOptimize[1])

    def optimize(
        self,
        *,
        maximize: Union[str, Callable[[pd.Series], float]] = "SQN",
        method: str = "grid",
        max_tries: Union[int, float] = None,
        constraint: Callable[[dict], bool] = None,
        return_heatmap: bool = False,
        return_optimization: bool = False,
        random_state: int = None,
        start_data_portion=0,
        end_data_portion=1,
        **kwargs,
    ) -> Union[
        pd.Series, Tuple[pd.Series, pd.Series], Tuple[pd.Series, pd.Series, dict]
    ]:
        """
        Optimize strategy parameters to an optimal combination.
        Returns result `pd.Series` of the best run.

        `maximize` is a string key from the
        `backtesting.backtesting.Backtest.run`-returned results series,
        or a function that accepts this series object and returns a number;
        the higher the better. By default, the method maximizes
        Van Tharp's [System Quality Number](https://google.com/search?q=System+Quality+Number).

        `method` is the optimization method. Currently two methods are supported:

        * `"grid"` which does an exhaustive (or randomized) search over the
          cartesian product of parameter combinations, and
        * `"skopt"` which finds close-to-optimal strategy parameters using
          [model-based optimization], making at most `max_tries` evaluations.

        [model-based optimization]: \
            https://scikit-optimize.github.io/stable/auto_examples/bayesian-optimization.html
        
        * `"genetic"` which finds close-to-optimal strategy parameters using
          genetic optimization.


        `max_tries` is the maximal number of strategy runs to perform.
        If `method="grid"`, this results in randomized grid search.
        If `max_tries` is a floating value between (0, 1], this sets the
        number of runs to approximately that fraction of full grid space.
        Alternatively, if integer, it denotes the absolute maximum number
        of evaluations. If unspecified (default), grid search is exhaustive,
        whereas for `method="skopt"`, `max_tries` is set to 200.

        `constraint` is a function that accepts a dict-like object of
        parameters (with values) and returns `True` when the combination
        is admissible to test with. By default, any parameters combination
        is considered admissible.

        If `return_heatmap` is `True`, besides returning the result
        series, an additional `pd.Series` is returned with a multiindex
        of all admissible parameter combinations, which can be further
        inspected or projected onto 2D to plot a heatmap
        (see `backtesting.lib.plot_heatmaps()`).

        If `return_optimization` is True and `method = 'skopt'`,
        in addition to result series (and maybe heatmap), return raw
        [`scipy.optimize.OptimizeResult`][OptimizeResult] for further
        inspection, e.g. with [scikit-optimize]\
        [plotting tools].

        [OptimizeResult]: \
            https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.OptimizeResult.html
        [scikit-optimize]: https://scikit-optimize.github.io
        [plotting tools]: https://scikit-optimize.github.io/stable/modules/plots.html

        If you want reproducible optimization results, set `random_state`
        to a fixed integer or a `numpy.random.RandomState` object.

        Additional keyword arguments represent strategy arguments with
        list-like collections of possible values. For example, the following
        code finds and returns the "best" of the 7 admissible (of the
        9 possible) parameter combinations:

            backtest.optimize(sma1=[5, 10, 15], sma2=[10, 20, 40],
                              constraint=lambda p: p.sma1 < p.sma2)

        .. TODO::
            Improve multiprocessing/parallel execution on Windos with start method 'spawn'.
        """
        if not kwargs:
            raise ValueError("Need some strategy parameters to optimize")

        # Custom Data Length
        datacopy = self._data.copy(deep=True)
        self._data = self._data[
            int(len(self._data) * start_data_portion) : int(
                len(self._data) * end_data_portion
            )
        ]

        maximize_key = None
        if isinstance(maximize, str):
            maximize_key = str(maximize)
            stats = self._results if self._results is not None else self.run()
            if maximize not in stats:
                raise ValueError(
                    "`maximize`, if str, must match a key in pd.Series "
                    "result of backtest.run()"
                )

            def maximize(stats: pd.Series, _key=maximize):
                return stats[_key]

        elif not callable(maximize):
            raise TypeError(
                "`maximize` must be str (a field of backtest.run() result "
                "Series) or a function that accepts result Series "
                "and returns a number; the higher the better"
            )

        have_constraint = bool(constraint)
        if constraint is None:

            def constraint(_):
                return True

        elif not callable(constraint):
            raise TypeError(
                "`constraint` must be a function that accepts a dict "
                "of strategy parameters and returns a bool whether "
                "the combination of parameters is admissible or not"
            )

        if return_optimization and method != "skopt":
            raise ValueError("return_optimization=True only valid if method='skopt'")

        if return_heatmap and method == "genetic":
            raise ValueError("return_heatmap=True only valid if method!='genetic'")

        def _tuple(x):
            return x if isinstance(x, Sequence) and not isinstance(x, str) else (x,)

        for k, v in kwargs.items():
            if len(_tuple(v)) == 0:
                raise ValueError(
                    f"Optimization variable '{k}' is passed no "
                    f"optimization values: {k}={v}"
                )

        class AttrDict(dict):
            def __getattr__(self, item):
                return self[item]

        def _grid_size():
            size = np.prod([len(_tuple(v)) for v in kwargs.values()])
            if size < 10_000 and have_constraint:
                size = sum(
                    1
                    for p in product(
                        *(zip(repeat(k), _tuple(v)) for k, v in kwargs.items())
                    )
                    if constraint(AttrDict(p))
                )
            return size

        def _optimize_grid() -> Union[pd.Series, Tuple[pd.Series, pd.Series]]:
            rand = np.random.RandomState(random_state).random
            grid_frac = (
                1
                if max_tries is None
                else max_tries
                if 0 < max_tries <= 1
                else max_tries / _grid_size()
            )
            param_combos = [
                dict(params)  # back to dict so it pickles
                for params in (
                    AttrDict(params)
                    for params in product(
                        *(zip(repeat(k), _tuple(v)) for k, v in kwargs.items())
                    )
                )
                if constraint(params) and rand() <= grid_frac  # type: ignore
            ]
            if not param_combos:
                raise ValueError("No admissible parameter combinations to test")

            if len(param_combos) > 300:
                warnings.warn(
                    f"Searching for best of {len(param_combos)} configurations.",
                    stacklevel=2,
                )

            heatmap = pd.Series(
                np.nan,
                name=maximize_key,
                index=pd.MultiIndex.from_tuples(
                    [p.values() for p in param_combos],
                    names=next(iter(param_combos)).keys(),
                ),
            )

            def _batch(seq):
                n = np.clip(int(len(seq) // (os.cpu_count() or 1)), 1, 300)
                for i in range(0, len(seq), n):
                    yield seq[i : i + n]

            # Save necessary objects into "global" state; pass into concurrent executor
            # (and thus pickle) nothing but two numbers; receive nothing but numbers.
            # With start method "fork", children processes will inherit parent address space
            # in a copy-on-write manner, achieving better performance/RAM benefit.
            backtest_uuid = np.random.random()
            param_batches = list(_batch(param_combos))
            Backtest._mp_backtests[backtest_uuid] = (self, param_batches, maximize)  # type: ignore
            try:
                # If multiprocessing start method is 'fork' (i.e. on POSIX), use
                # a pool of processes to compute results in parallel.
                # Otherwise (i.e. on Windos), sequential computation will be "faster".
                if mp.get_start_method(allow_none=False) == "fork":
                    with ProcessPoolExecutor() as executor:
                        futures = [
                            executor.submit(Backtest._mp_task, backtest_uuid, i)
                            for i in range(len(param_batches))
                        ]
                        for future in _tqdm(
                            as_completed(futures),
                            total=len(futures),
                            desc="Backtest.optimize",
                        ):
                            batch_index, values = future.result()
                            for value, params in zip(
                                values, param_batches[batch_index]
                            ):
                                heatmap[tuple(params.values())] = value
                else:
                    if os.name == "posix":
                        warnings.warn(
                            "For multiprocessing support in `Backtest.optimize()` "
                            "set multiprocessing start method to 'fork'."
                        )
                    for batch_index in _tqdm(range(len(param_batches))):
                        _, values = Backtest._mp_task(backtest_uuid, batch_index)
                        for value, params in zip(values, param_batches[batch_index]):
                            heatmap[tuple(params.values())] = value
            finally:
                del Backtest._mp_backtests[backtest_uuid]

            best_params = heatmap.idxmax()

            if pd.isnull(best_params):
                # No trade was made in any of the runs. Just make a random
                # run so we get some, if empty, results
                stats = self.run(**param_combos[0])
            else:
                stats = self.run(**dict(zip(heatmap.index.names, best_params)))

            if return_heatmap:
                return [stats, heatmap]
            return [stats]

        def _optimize_skopt() -> Union[
            pd.Series, Tuple[pd.Series, pd.Series], Tuple[pd.Series, pd.Series, dict]
        ]:
            try:
                from skopt import forest_minimize
                from skopt.space import Integer, Real, Categorical
                from skopt.utils import use_named_args
                from skopt.callbacks import DeltaXStopper
                from skopt.learning import ExtraTreesRegressor
            except ImportError:
                raise ImportError(
                    "Need package 'scikit-optimize' for method='skopt'. "
                    "pip install scikit-optimize"
                )

            nonlocal max_tries
            max_tries = (
                200
                if max_tries is None
                else max(1, int(max_tries * _grid_size()))
                if 0 < max_tries <= 1
                else max_tries
            )

            dimensions = []
            for key, values in kwargs.items():
                values = np.asarray(values)
                if values.dtype.kind in "mM":  # timedelta, datetime64
                    # these dtypes are unsupported in skopt, so convert to raw int
                    # TODO: save dtype and convert back later
                    values = values.astype(int)

                if values.dtype.kind in "iumM":
                    dimensions.append(
                        Integer(low=values.min(), high=values.max(), name=key)
                    )
                elif values.dtype.kind == "f":
                    dimensions.append(
                        Real(low=values.min(), high=values.max(), name=key)
                    )
                else:
                    dimensions.append(
                        Categorical(values.tolist(), name=key, transform="onehot")
                    )

            # Avoid recomputing re-evaluations:
            # "The objective has been evaluated at this point before."
            # https://github.com/scikit-optimize/scikit-optimize/issues/302
            memoized_run = lru_cache()(lambda tup: self.run(**dict(tup)))

            # np.inf/np.nan breaks sklearn, np.finfo(float).max breaks skopt.plots.plot_objective
            INVALID = 1e300
            progress = iter(
                _tqdm(repeat(None), total=max_tries, desc="Backtest.optimize")
            )

            @use_named_args(dimensions=dimensions)
            def objective_function(**params):
                next(progress)
                # Check constraints
                # TODO: Adjust after https://github.com/scikit-optimize/scikit-optimize/pull/971
                if not constraint(AttrDict(params)):
                    return INVALID
                res = memoized_run(tuple(params.items()))
                value = -maximize(res)
                if np.isnan(value):
                    return INVALID
                return value

            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore", "The objective has been evaluated at this point before."
                )

                res = forest_minimize(
                    func=objective_function,
                    dimensions=dimensions,
                    n_calls=max_tries,
                    base_estimator=ExtraTreesRegressor(
                        n_estimators=20, min_samples_leaf=2
                    ),
                    acq_func="LCB",
                    kappa=3,
                    n_initial_points=min(max_tries, 20 + 3 * len(kwargs)),
                    initial_point_generator="lhs",  # 'sobel' requires n_initial_points ~ 2**N
                    callback=DeltaXStopper(9e-7),
                    random_state=random_state,
                )

            stats = self.run(**dict(zip(kwargs.keys(), res.x)))
            output = [stats]

            if return_heatmap:
                heatmap = pd.Series(
                    dict(zip(map(tuple, res.x_iters), -res.func_vals)),
                    name=maximize_key,
                )
                heatmap.index.names = kwargs.keys()
                heatmap = heatmap[heatmap != -INVALID]
                heatmap.sort_index(inplace=True)
                output.append(heatmap)

            if return_optimization:
                valid = res.func_vals != INVALID
                res.x_iters = list(compress(res.x_iters, valid))
                res.func_vals = res.func_vals[valid]
                output.append(res)

            return stats if len(output) == 1 else tuple(output)

        def _optimize_genetic() -> Union[pd.Series]:
            try:
                from geneticalgorithm import geneticalgorithm
            except ImportError:
                raise ImportError(
                    "Need package 'geneticalgorithm' for method='genetic'. "
                    "pip install geneticalgorithm"
                )

            nonlocal max_tries
            max_tries = (
                200
                if max_tries is None
                else max(1, int(max_tries * _grid_size()))
                if 0 < max_tries <= 1
                else max_tries
            )

            dimensions = []
            dimensionstype = []
            for key, values in kwargs.items():
                values = np.asarray(values)
                dimensions.append([values.min(), values.max()])

                if values.dtype.kind in "mM":  # timedelta, datetime64
                    # these dtypes are unsupported in skopt, so convert to raw int
                    # TODO: save dtype and convert back later
                    values = values.astype(int)

                if values.dtype.kind in "iumM":
                    dimensionstype.append(["int"])
                elif values.dtype.kind == "f":
                    dimensions.append(["real"])
                else:
                    dimensions.append(["bool"])

            def objective_function(params):
                return -1 * self.run(**dict(zip(kwargs.keys(), params)))[maximize_key]

            with warnings.catch_warnings():
                warnings.filterwarnings(
                    "ignore",
                    "GA is terminated due to the maximum number of iterations without improvement was met!",
                )
                algorithm_param = {
                    "max_num_iteration": int(max_tries),
                    "population_size": int(max_tries / 10),
                    "mutation_probability": 0.1,
                    "elit_ratio": 0.01,
                    "crossover_probability": 0.5,
                    "parents_portion": 0.3,
                    "crossover_type": "uniform",
                    "max_iteration_without_improv": int(max_tries / 4),
                }

                model = geneticalgorithm(
                    function=objective_function,
                    dimension=len(dimensions),
                    variable_type_mixed=np.array(dimensionstype),
                    variable_boundaries=np.array(dimensions),
                    algorithm_parameters=algorithm_param,
                    convergence_curve=False,
                    progress_bar=True,
                )

                model.run()

            stats = self.run(**dict(zip(kwargs.keys(), model.best_variable)))
            output = [stats]

            return stats if len(output) == 1 else tuple(output)

        if method == "grid":
            output = _optimize_grid()
        elif method == "skopt":
            output = _optimize_skopt()
        elif method == "genetic":
            output = _optimize_genetic()
        else:
            raise ValueError(
                f"Method should be 'grid' or 'skopt' or 'genetic', not {method!r}"
            )

        # Restore Data
        self._data = datacopy
        values = [getattr(output[0]._strategy, kwarg) for kwarg in kwargs.keys()]

        return output, dict(zip(kwargs.keys(), values))

    @staticmethod
    def _mp_task(backtest_uuid, batch_index):
        bt, param_batches, maximize_func = Backtest._mp_backtests[backtest_uuid]
        return batch_index, [
            maximize_func(stats) if stats["# Trades"] else np.nan
            for stats in (bt.run(**params) for params in param_batches[batch_index])
        ]

    _mp_backtests: Dict[float, Tuple["Backtest", List, Callable]] = {}

    @staticmethod
    def _compute_drawdown_duration_peaks(dd: pd.Series):
        iloc = np.unique(np.r_[(dd == 0).values.nonzero()[0], len(dd) - 1])
        iloc = pd.Series(iloc, index=dd.index[iloc])
        df = iloc.to_frame("iloc").assign(prev=iloc.shift())
        df = df[df["iloc"] > df["prev"] + 1].astype(int)
        # If no drawdown since no trade, avoid below for pandas sake and return nan series
        if not len(df):
            return (dd.replace(0, np.nan),) * 2
        df["duration"] = df["iloc"].map(dd.index.__getitem__) - df["prev"].map(
            dd.index.__getitem__
        )
        df["peak_dd"] = df.apply(
            lambda row: dd.iloc[row["prev"] : row["iloc"] + 1].max(), axis=1
        )
        df = df.reindex(dd.index)
        return df["duration"], df["peak_dd"]

    def _compute_stats(self, broker: _Broker, strategy: Strategy) -> pd.Series:
        data = self._data
        index = data.index

        equity = (
            pd.Series(broker._equity)
            .bfill()
            .fillna(broker._cash)
            .values[: len(self._data)]
        )
        dd = 1 - equity / np.maximum.accumulate(equity)
        dd_dur, dd_peaks = self._compute_drawdown_duration_peaks(
            pd.Series(dd, index=index)
        )

        equity_df = pd.DataFrame(
            {"Equity": equity, "DrawdownPct": dd, "DrawdownDuration": dd_dur},
            index=index,
        )

        trades = broker.closed_trades
        trades_df = pd.DataFrame(
            {
                "Size": [t.size for t in trades],
                "EntryBar": [t.entry_bar for t in trades],
                "ExitBar": [t.exit_bar for t in trades],
                "EntryPrice": [t.entry_price for t in trades],
                "ExitPrice": [t.exit_price for t in trades],
                "PnL": [t.pl for t in trades],
                "ReturnPct": [t.pl_pct for t in trades],
                "EntryTime": [t.entry_time for t in trades],
                "ExitTime": [t.exit_time for t in trades],
            }
        )
        trades_df["Duration"] = trades_df["ExitTime"] - trades_df["EntryTime"]

        pl = trades_df["PnL"]
        returns = trades_df["ReturnPct"]
        durations = trades_df["Duration"]

        def _round_timedelta(value, _period=_data_period(index)):
            if not isinstance(value, pd.Timedelta):
                return value
            resolution = (
                getattr(_period, "resolution_string", None) or _period.resolution
            )
            return value.ceil(resolution)

        s = pd.Series(dtype=object)
        s.loc["Start"] = index[0]
        s.loc["End"] = index[-1]
        s.loc["Duration"] = s.End - s.Start

        have_position = np.repeat(0, len(index))
        for t in trades:
            have_position[t.entry_bar : t.exit_bar + 1] = 1  # type: ignore

        s.loc["Exposure Time [%]"] = (
            have_position.mean() * 100
        )  # In "n bars" time, not index time
        s.loc["Equity Final [$]"] = equity[-1]
        s.loc["Equity Peak [$]"] = equity.max()
        s.loc["Return [%]"] = (equity[-1] - equity[0]) / equity[0] * 100
        c = data.Close.values
        s.loc["Buy & Hold Return [%]"] = (c[-1] - c[0]) / c[0] * 100  # long-only return

        def geometric_mean(returns):
            returns = returns.fillna(0) + 1
            return (
                0
                if np.any(returns <= 0)
                else np.exp(np.log(returns).sum() / (len(returns) or np.nan)) - 1
            )

        day_returns = gmean_day_return = np.array(np.nan)
        annual_trading_days = np.nan
        if isinstance(index, pd.DatetimeIndex):
            day_returns = equity_df["Equity"].resample("D").last().dropna().pct_change()
            gmean_day_return = geometric_mean(day_returns)
            annual_trading_days = float(
                365
                if index.dayofweek.to_series().between(5, 6).mean() > 2 / 7 * 0.6
                else 252
            )

        # Annualized return and risk metrics are computed based on the (mostly correct)
        # assumption that the returns are compounded. See: https://dx.doi.org/10.2139/ssrn.3054517
        # Our annualized return matches `empyrical.annual_return(day_returns)` whereas
        # our risk doesn't; they use the simpler approach below.
        annualized_return = (1 + gmean_day_return) ** annual_trading_days - 1
        s.loc["Return (Ann.) [%]"] = annualized_return * 100
        s.loc["Volatility (Ann.) [%]"] = (
            np.sqrt(
                (
                    day_returns.var(ddof=int(bool(day_returns.shape)))
                    + (1 + gmean_day_return) ** 2
                )
                ** annual_trading_days
                - (1 + gmean_day_return) ** (2 * annual_trading_days)
            )
            * 100
        )  # noqa: E501
        # s.loc['Return (Ann.) [%]'] = gmean_day_return * annual_trading_days * 100
        # s.loc["Risk (Ann.) [%]"] = (
        #     day_returns.std(ddof=1) * np.sqrt(annual_trading_days) * 100
        # )

        # Our Sharpe mismatches `empyrical.sharpe_ratio()` because they use arithmetic mean return
        # and simple standard deviation
        s.loc["Sharpe Ratio"] = np.clip(
            s.loc["Return (Ann.) [%]"] / (s.loc["Volatility (Ann.) [%]"] or np.nan),
            0,
            np.inf,
        )  # noqa: E501
        # Our Sortino mismatches `empyrical.sortino_ratio()` because they use arithmetic mean return
        s.loc["Sortino Ratio"] = np.clip(
            annualized_return
            / (
                np.sqrt(np.mean(day_returns.clip(-np.inf, 0) ** 2))
                * np.sqrt(annual_trading_days)
            ),
            0,
            np.inf,
        )  # noqa: E501
        max_dd = -np.nan_to_num(dd.max())
        s.loc["Calmar Ratio"] = np.clip(
            annualized_return / (-max_dd or np.nan), 0, np.inf
        )
        s.loc["Max. Drawdown [%]"] = max_dd * 100
        s.loc["Avg. Drawdown [%]"] = -dd_peaks.mean() * 100
        s.loc["Max. Drawdown Duration"] = _round_timedelta(dd_dur.max())
        s.loc["Avg. Drawdown Duration"] = _round_timedelta(dd_dur.mean())
        s.loc["# Trades"] = n_trades = len(trades)
        s.loc["Win Rate [%]"] = (
            np.nan if not n_trades else (pl > 0).sum() / n_trades * 100
        )  # noqa: E501
        s.loc["Best Trade [%]"] = returns.max() * 100
        s.loc["Worst Trade [%]"] = returns.min() * 100
        mean_return = geometric_mean(returns)
        s.loc["Avg. Trade [%]"] = mean_return * 100
        s.loc["Max. Trade Duration"] = _round_timedelta(durations.max())
        s.loc["Avg. Trade Duration"] = _round_timedelta(durations.mean())
        s.loc["Profit Factor"] = returns[returns > 0].sum() / (
            abs(returns[returns < 0].sum()) or np.nan
        )  # noqa: E501
        s.loc["Win/Loss Ratio"] = returns[returns > 0].mean() / (
            abs(returns[returns < 0].mean()) or np.nan
        )  # noqa: E501
        s.loc["Expectancy [%]"] = returns.mean() * 100
        s.loc["SQN"] = np.sqrt(n_trades) * pl.mean() / (pl.std() or np.nan)
        s.loc["_strategy"] = strategy
        s.loc["_equity_curve"] = equity_df
        s.loc["_pnl_curve"] = (
            pd.Series(broker._equity).dropna().drop_duplicates().values
        )
        s.loc["_average_curve"] = (
            pd.Series(broker._equity)
            .dropna()
            .drop_duplicates()
            .rolling(50)
            .mean()
            .values
        )
        s.loc["_trades"] = trades_df

        s = Backtest._Stats(s)
        return s

    class _Stats(pd.Series):
        def __repr__(self):
            # Prevent expansion due to _equity and _trades dfs
            with pd.option_context("max_colwidth", 20):
                return super().__repr__()

    def plot(
        self,
        *,
        results: pd.Series = None,
        filename=None,
        plot_width=None,
        plot_equity=True,
        plot_return=False,
        plot_pl=True,
        plot_volume=True,
        plot_drawdown=False,
        smooth_equity=False,
        relative_equity=True,
        superimpose: Union[bool, str] = True,
        resample=True,
        reverse_indicators=False,
        show_legend=True,
        open_browser=True,
    ):
        """
        Plot the progression of the last backtest run.

        If `results` is provided, it should be a particular result
        `pd.Series` such as returned by
        `backtesting.backtesting.Backtest.run` or
        `backtesting.backtesting.Backtest.optimize`, otherwise the last
        run's results are used.

        `filename` is the path to save the interactive HTML plot to.
        By default, a strategy/parameter-dependent file is created in the
        current working directory.

        `plot_width` is the width of the plot in pixels. If None (default),
        the plot is made to span 100% of browser width. The height is
        currently non-adjustable.

        If `plot_equity` is `True`, the resulting plot will contain
        an equity (initial cash plus assets) graph section. This is the same
        as `plot_return` plus initial 100%.

        If `plot_return` is `True`, the resulting plot will contain
        a cumulative return graph section. This is the same
        as `plot_equity` minus initial 100%.

        If `plot_pl` is `True`, the resulting plot will contain
        a profit/loss (P/L) indicator section.

        If `plot_volume` is `True`, the resulting plot will contain
        a trade volume section.

        If `plot_drawdown` is `True`, the resulting plot will contain
        a separate drawdown graph section.

        If `smooth_equity` is `True`, the equity graph will be
        interpolated between fixed points at trade closing times,
        unaffected by any interim asset volatility.

        If `relative_equity` is `True`, scale and label equity graph axis
        with return percent, not absolute cash-equivalent values.

        If `superimpose` is `True`, superimpose larger-timeframe candlesticks
        over the original candlestick chart. Default downsampling rule is:
        monthly for daily data, daily for hourly data, hourly for minute data,
        and minute for (sub-)second data.
        `superimpose` can also be a valid [Pandas offset string],
        such as `'5T'` or `'5min'`, in which case this frequency will be
        used to superimpose.
        Note, this only works for data with a datetime index.

        If `resample` is `True`, the OHLC data is resampled in a way that
        makes the upper number of candles for Bokeh to plot limited to 10_000.
        This may, in situations of overabundant data,
        improve plot's interactive performance and avoid browser's
        `Javascript Error: Maximum call stack size exceeded` or similar.
        Equity & dropdown curves and individual trades data is,
        likewise, [reasonably _aggregated_][TRADES_AGG].
        `resample` can also be a [Pandas offset string],
        such as `'5T'` or `'5min'`, in which case this frequency will be
        used to resample, overriding above numeric limitation.
        Note, all this only works for data with a datetime index.

        If `reverse_indicators` is `True`, the indicators below the OHLC chart
        are plotted in reverse order of declaration.

        [Pandas offset string]: \
            https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#dateoffset-objects

        [TRADES_AGG]: lib.html#backtesting.lib.TRADES_AGG

        If `show_legend` is `True`, the resulting plot graphs will contain
        labeled legends.

        If `open_browser` is `True`, the resulting `filename` will be
        opened in the default web browser.
        """
        if results is None:
            if self._results is None:
                raise RuntimeError("First issue `backtest.run()` to obtain results.")
            results = self._results

        plot(
            results=results,
            df=self._data,
            indicators=results._strategy._indicators,
            filename=filename,
            plot_width=plot_width,
            plot_equity=plot_equity,
            plot_return=plot_return,
            plot_pl=plot_pl,
            plot_volume=plot_volume,
            plot_drawdown=plot_drawdown,
            smooth_equity=smooth_equity,
            relative_equity=relative_equity,
            superimpose=superimpose,
            resample=resample,
            reverse_indicators=reverse_indicators,
            show_legend=show_legend,
            open_browser=open_browser,
        )

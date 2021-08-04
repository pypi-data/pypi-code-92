from abc import ABC
import ast
from typing import List, Union, Tuple, Any
from collections import Counter
import numpy as np
import itertools
from collections import OrderedDict
from .rule import Rule
from .activation import Activation

try:
    import pandas as pd
    pandas_ok = True
except ImportError:
    class pd:
        DataFrame = None
        Series = None
    pandas_ok = False


class RuleSet(ABC):

    """A set of rules"""

    NLINES = 5  # half how many rules to show in str(self)
    CHECK_DUPLICATED = False
    all_features_indexes = {}

    @staticmethod
    def check_duplicated_rules(rules, name_or_index: str = "index"):
        if name_or_index == "index":
            str_rules = [str(r.features_indexes) + str(r.bmins) + str(r.bmaxs) for r in rules]
        else:
            str_rules = [str(r.features_names) + str(r.bmins) + str(r.bmaxs) for r in rules]
        if len(set(str_rules)) < len(str_rules):
            duplicated = {}
            for r in str_rules:
                if r not in duplicated:
                    duplicated[r] = 0
                duplicated[r] += 1
            duplicated = [
                f"{r}: {duplicated[r]} (positions {[i for i, x in enumerate(str_rules) if x == r]})\n"
                f"   underlying rules : {[str(rules[i]) for i in [i for i, x in enumerate(str_rules) if x == r]]}"
                for r in duplicated
                if duplicated[r] > 1
            ]
            s = "\n -".join(duplicated)
            raise ValueError(f"There are {len(duplicated)} duplicated rules in your ruleset !\n {s}")

    def __init__(
        self,
        rules_list: Union[List[Rule], None] = None,
        remember_activation: bool = True,
        stack_activation: bool = False,
    ):
        """

        Parameters
        ----------
        rules_list: Union[List[Rule], None]
            The list of rules to start with. Can be None, since a RuleSet can be filled after its creation.
        remember_activation: bool
            The activation of the RuleSet is the logical OR of the activation of all its rules. It is only computed
            if remember_activation is True. (default value = True)
        stack_activation: bool
            If True, the RuleSet will keep in memory 2-D np.ndarray containing the activations of all its rules. This
            can take a lot of memory, but can save time if you apply numpy methods on this stacked vector instead of on
            each rule separately. (default value = False)
        """
        self._rules = []
        self.features_names = []
        self.features_indexes = []
        self._activation = None
        self.stacked_activations = None
        self.remember_activation = remember_activation
        self.stack_activation = stack_activation
        if rules_list is not None:
            names_available = all([hasattr(r.condition, "features_names") for r in self])
            for rule in rules_list:
                if not isinstance(rule, Rule) and rule is not None:
                    raise TypeError(f"Some rules in given iterable were not of type 'Rule' but of type {type(rule)}")
                if rule is not None:
                    self.append(rule, update_activation=False)
            if self.remember_activation:
                self.compute_self_activation()
            if self.stack_activation:
                self.compute_stacked_activation()
            if names_available:
                self.features_names = list(set(itertools.chain(*[rule.features_names for rule in self])))
            self.set_features_indexes()
        if RuleSet.CHECK_DUPLICATED:
            self.check_duplicated_rules(self.rules, name_or_index="name" if len(self.features_names) > 0 else "index")

    @property
    def rules(self) -> List[Rule]:
        return self._rules

    @rules.setter
    def rules(self, rules: Union[List[Rule], None]):
        ruleset = RuleSet(rules, remember_activation=self.remember_activation, stack_activation=self.stack_activation)
        self._rules = ruleset._rules
        self.features_names = ruleset.features_names
        self.features_indexes = ruleset.features_indexes
        self.stacked_activations = ruleset.stacked_activations
        self._activation = ruleset._activation

    def set_features_indexes(self):
        if len(RuleSet.all_features_indexes) > 0:
            self.features_indexes = [RuleSet.all_features_indexes[f] for f in self.features_names]
            for r in self._rules:
                # noinspection PyProtectedMember
                r._condition._features_indexes = [RuleSet.all_features_indexes[f] for f in r.features_names]
        else:
            list(set(itertools.chain(*[rule.features_indexes for rule in self])))

    # noinspection PyProtectedMember,PyTypeChecker
    def __iadd__(self, other: Union["RuleSet", Rule]):
        """Appends a rule or each rules of another RuleSet to self and updates activation vector and stacked activations
        if needed. Also updates features_indexes, and features_names if possible."""
        if isinstance(other, Rule):
            self._rules.append(other)
        else:
            self._rules += other._rules
        self.features_indexes = list(set(self.features_indexes + other.features_indexes))
        if hasattr(other, "features_names"):
            self.features_names = list(set(self.features_names + other.features_names))
        if self.remember_activation:
            self._update_activation(other)
        if self.stack_activation:
            self._update_stacked_activation(other)
        return self

    def __add__(self, other: Union["RuleSet", Rule]):
        """Returns the RuleSet resulting in appendind a rule or each rules of another RuleSet to self."""
        remember_activation = self.remember_activation
        stack_activation = self.stack_activation
        if isinstance(other, Rule):
            rules = self.rules + [other]
        else:
            remember_activation &= other.remember_activation
            stack_activation &= other.stack_activation
            rules = list(set(self.rules + other.rules))
        return self.__class__(rules, remember_activation=remember_activation, stack_activation=stack_activation)

    def __getattr__(self, item):
        """If item is not found in self, try to fetch it from its activation."""
        if item == "_activation":
            raise AttributeError(f"'RuleSet' object has no attribute '{item}'")

        if self._activation is not None and hasattr(self._activation, item):
            return getattr(self._activation, item)
        raise AttributeError(f"'RuleSet' object has no attribute '{item}'")

    def __len__(self):
        """The length of a RuleSet its the number of rules stored in it."""
        return len(self.rules)

    def __eq__(self, other: "RuleSet"):
        return set(self.rules) == set(other.rules)

    def __iter__(self):
        if hasattr(self, "_rules"):
            return self.rules.__iter__()
        else:
            return [].__iter__()

    def __getitem__(self, key):
        if isinstance(key, slice):
            indices = range(*key.indices(len(self.rules)))
            return self.__class__([self.rules[i] for i in indices])
        return self.rules.__getitem__(key)

    def __str__(self):
        if len(self) < 2 * RuleSet.NLINES:
            return "\n".join([str(self[i]) for i in range(len(self))])
        else:
            return "\n".join(
                [str(self[i]) for i in range(RuleSet.NLINES)]
                + ["..."]
                + [str(self[i]) for i in range(len(self) - RuleSet.NLINES, len(self))]
            )

    @property
    def to_hash(self) -> Tuple[str]:
        if len(self) == 0:
            return "rs",
        to_hash = ("rs",)
        for r in self:
            rule_hash = r.to_hash[1:]
            to_hash += rule_hash
        return to_hash

    def __hash__(self) -> hash:
        return hash(frozenset(self.to_hash))

    # noinspection PyProtectedMember,PyTypeChecker
    def _update_activation(self, other: Union[Rule, "RuleSet"]):
        """Updates the activation vector of the RuleSet with the activation vector of a new Rule or RuleSet."""
        if other.activation_available:
            if self._activation is None:
                self._activation = Activation(other.activation, to_file=Rule.LOCAL_ACTIVATION)
            else:
                self._activation = self._activation | other._activation

    # noinspection PyProtectedMember,PyTypeChecker
    def _update_stacked_activation(self, other: Union[Rule, "RuleSet"]):
        """Updates the stacked activation vectors of the RuleSet with the activation vector of a new Rule or
         the stacked activation vectors of another RuleSet."""
        if other.activation_available:
            if not pandas_ok:
                raise ImportError("RuleSet's stacked activations requied pandas. Please run\npip install pandas")
            if self._activation is None:
                if isinstance(other, Rule):
                    self.stacked_activations = pd.DataFrame(data=np.array(other.activation).T, columns=[str(other)])
                else:
                    self.stacked_activations = other.stacked_activations
            else:
                if isinstance(other, Rule):
                    self.stacked_activations[str(other)] = other.activation
                else:
                    self.stacked_activations = pd.concat([self.stacked_activations, other.stacked_activations], axis=1)

    def compute_self_activation(self):
        """Computes the activation vector of self from its rules, using time-efficient Activation.multi_logical_or."""
        if len(self) == 0:
            return
        activations_available = all([r.activation_available for r in self])
        if activations_available:
            # noinspection PyProtectedMember
            self._activation = Activation.multi_logical_or([r._activation for r in self])

    def compute_stacked_activation(self):
        """Computes the stacked activation vectors of self from its rules."""
        if len(self) == 0:
            return
        if not pandas_ok:
            raise ImportError("RuleSet's stacked activations requied pandas. Please run\npip install pandas")
        activations_available = all([r.activation_available for r in self])
        if activations_available:
            # noinspection PyProtectedMember
            self.stacked_activations = pd.DataFrame(
                data=np.array([r.activation for r in self]).T, columns=[str(r.condition) for r in self]
            )

    # def __del__(self):
    #     self.del_activations()
    #     self.del_activation()

    def del_activations(self):
        """Deletes the data, but not the relevent attributes, of the activation vector or each rules in self."""
        for r in self:
            r.del_activation()

    def del_activation(self):
        """Deletes the activation vector's data of self, but not the object itself, so any computed attribute remains
        available"""
        if hasattr(self, "_activation") and self._activation is not None:
            self._activation.delete()

    def del_stacked_activations(self):
        """Deletes stacked activation vectors of self. Set it to None."""
        if hasattr(self, "stacked_activations") and self.stacked_activations is not None:
            del self.stacked_activations
            self.stacked_activations = None

    def append(self, rule: Rule, update_activation: bool = True):
        """Appends a new rule to self. The updates of activation vector and the stacked activation vectors can be
        blocked by specifying update_activation=False. Otherwise, will use self.remember_activation and
        self.stack_activation to determine if the updates should be done or not."""
        if not isinstance(rule, Rule):
            raise TypeError(f"RuleSet's append method expects a Rule object, got {type(rule)}")
        remember_activation = self.remember_activation
        stack_activation = self.stack_activation
        if not update_activation:
            self.remember_activation = False
            self.stack_activation = False
        self.__iadd__(rule)
        self.remember_activation = remember_activation
        self.stack_activation = stack_activation

    def sort(self, criterion: str = None, reverse: bool = False):
        """Sorts the RuleSet.

        * If criterion is not speficied:
            Will sort the rules according to :
                1. The number of features they talk about
                2. For a same number of features (sorted in alphabetical order, or index if names are not available,
                    optionally reversed), the bmins and bmaxs of the rules
        * If criterion is specified, it must be an float or interger attribute of rule, condition or activation. Then
            sorts according to this criterion, optionally reversed.
        """
        if len(self) == 0:
            return

        if criterion is None or criterion == "":
            if not (
                hasattr(self[0].condition, "bmins")
                and hasattr(self[0].condition, "bmaxs")
            ):
                return
            # The set of all the features the RuleSet talks about
            which = "index"
            if len(self.features_names) > 0:
                which = "name"
                fnames_or_indexes = list(set([str(r.features_names) for r in self]))
            else:
                fnames_or_indexes = list(set([str(r.features_indexes) for r in self]))
            dict_names = {}
            lmax = 1
            for f in fnames_or_indexes:
                l_ = len(ast.literal_eval(f))
                if l_ > lmax:
                    lmax = l_
                if l_ not in dict_names:
                    dict_names[l_] = []
                dict_names[l_].append(f)
            for l_ in dict_names:
                dict_names[l_].sort(reverse=reverse)
            fnames_or_indexes = []
            for l_ in range(1, lmax + 1):
                if l_ in dict_names:
                    fnames_or_indexes += dict_names[l_]

            rules_by_fnames = OrderedDict({f: [] for f in fnames_or_indexes})
            for rule in self:
                # noinspection PyUnresolvedReferences
                if which == "name":
                    v = str(rule.features_names)
                else:
                    v = str(rule.features_indexes)
                rules_by_fnames[v].append(rule)
            rules_by_fnames = {
                n: sorted(rules_by_fnames[n], key=lambda x: x.condition.bmins + x.condition.bmaxs)
                for n in rules_by_fnames
            }
            self._rules = []
            for n in rules_by_fnames:
                self._rules += rules_by_fnames[n]
        elif hasattr(self[0], criterion):
            self._rules = sorted(self, key=lambda x: getattr(x, criterion), reverse=reverse)
        else:
            raise ValueError(f"Can not sort RuleSet according to criterion {criterion}")
        if self.stack_activation:
            self.stacked_activations = self.stacked_activations[[str(r.condition) for r in self]]

    # noinspection PyProtectedMember
    def __contains__(self, other: Union["RuleSet", Rule]) -> bool:
        """A RuleSet contains another Rule or RuleSet if the second Rule or RuleSet activated points are also all
         activated by the first RuleSet."""
        if not self._activation or not other._activation:
            return False
        return other._activation in self._activation

    @property
    def activation_available(self) -> bool:
        """Returns True if the RuleSet has an activation vector, and if this Activation's object data is available."""
        if self._activation is None:
            return False
        if self._activation.data_format == "file":
            return self._activation.data.is_file()
        else:
            return self._activation.data is not None

    @property
    def stacked_activations_available(self) -> bool:
        """Returns True is the RuleSet has its rules' stacked activations."""
        if self.stack_activation is None:
            return False
        return True

    @property
    def activation(self) -> Union[None, np.ndarray]:
        """Returns the Activation vector's data in a form of a 1-D np.ndarray, or None if not available.

        Returns:
        --------
        Union[None, np.ndarray]
            of the form [0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, ...]
        """
        if self._activation:
            return self._activation.raw
        return None

    def calc_activation(self, xs: np.ndarray):
        """Uses input xs features data to compute the activation vector of all rules in self, and updates self's
        activation if self.remember_activation is True and stacked activation if self.stack_activation is True"""
        if len(self) == 0:
            raise ValueError("Can not use calc_activation : The ruleset is empty!")
        [rule.calc_activation(xs) for rule in self.rules]

        if self.remember_activation:
            self._activation = None
            self.compute_self_activation()
        if self.stack_activation:
            self.stacked_activations = None
            self.compute_stacked_activation()

    @property
    def coverage(self) -> float:
        """Coverage is the fraction of points equal to 1 in the activation vector"""
        if not self.activation_available:
            return 0.0
        else:
            return self._activation.coverage

    def get_features_count(self) -> List[Tuple[Any, int]]:
        """
        Get a counter of all different features in the ruleset. If names are not available, will use indexes.

        Returns:
        --------
        count : List[Tuple[Any, int]]
            Counter of all different features in the ruleset
        """
        # noinspection PyUnresolvedReferences
        if len(self) == 0:
            return []
        if len(self.features_names) > 0:
            var_in = list(itertools.chain(*[rule.features_names for rule in self]))
        else:
            var_in = list(itertools.chain(*[rule.feautres_indexes for rule in self]))
        count = Counter(var_in)

        count = count.most_common()
        return count

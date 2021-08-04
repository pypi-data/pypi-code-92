"""Lunisolar calendar calculations.

See trading_calendars/etc/lunisolar for code to calculate
"""

import pandas as pd


# Precomputed Chinese Lunar Year dates.
# Also called Spring Festival
#
# See Also
# --------
# trading_calendars/etc/lunisolar chinese-new-year
chinese_lunar_new_year_dates = pd.to_datetime(
    [
        "1960-01-28",
        "1961-02-15",
        "1962-02-05",
        "1963-01-25",
        "1964-02-13",
        "1965-02-02",
        "1966-01-21",
        "1967-02-09",
        "1968-01-30",
        "1969-02-17",
        "1970-02-06",
        "1971-01-27",
        "1972-02-15",
        "1973-02-03",
        "1974-01-23",
        "1975-02-11",
        "1976-01-31",
        "1977-02-18",
        "1978-02-07",
        "1979-01-28",
        "1980-02-16",
        "1981-02-05",
        "1982-01-25",
        "1983-02-13",
        "1984-02-02",
        "1985-02-20",
        "1986-02-09",
        "1987-01-29",
        "1988-02-17",
        "1989-02-06",
        "1990-01-27",
        "1991-02-15",
        "1992-02-04",
        "1993-01-23",
        "1994-02-10",
        "1995-01-31",
        "1996-02-19",
        "1997-02-07",
        "1998-01-28",
        "1999-02-16",
        "2000-02-05",
        "2001-01-24",
        "2002-02-12",
        "2003-02-01",
        "2004-01-22",
        "2005-02-09",
        "2006-01-29",
        "2007-02-18",
        "2008-02-07",
        "2009-01-26",
        "2010-02-14",
        "2011-02-03",
        "2012-01-23",
        "2013-02-10",
        "2014-01-31",
        "2015-02-19",
        "2016-02-08",
        "2017-01-28",
        "2018-02-16",
        "2019-02-05",
        "2020-01-25",
        "2021-02-12",
        "2022-02-01",
        "2023-01-22",
        "2024-02-10",
        "2025-01-29",
        "2026-02-17",
        "2027-02-06",
        "2028-01-26",
        "2029-02-13",
        "2030-02-03",
        "2031-01-23",
        "2032-02-11",
        "2033-01-31",
        "2034-02-19",
        "2035-02-08",
        "2036-01-28",
        "2037-02-15",
        "2038-02-04",
        "2039-01-24",
        "2040-02-12",
        "2041-02-01",
        "2042-01-22",
        "2043-02-10",
        "2044-01-30",
        "2045-02-17",
        "2046-02-06",
        "2047-01-26",
        "2048-02-14",
        "2049-02-02",
    ]
)

# Precomputed Qingming Festival dates.
# Also called Tomb-sweeping Day
#
# See Also
# --------
# trading_calendars/etc/lunisolar qingming-festival
qingming_festival_dates = pd.to_datetime(
    [
        "1960-04-05",
        "1961-04-05",
        "1962-04-05",
        "1963-04-05",
        "1964-04-05",
        "1965-04-05",
        "1966-04-05",
        "1967-04-05",
        "1968-04-05",
        "1969-04-05",
        "1970-04-05",
        "1971-04-05",
        "1972-04-05",
        "1973-04-05",
        "1974-04-05",
        "1975-04-05",
        "1976-04-04",
        "1977-04-05",
        "1978-04-05",
        "1979-04-05",
        "1980-04-04",
        "1981-04-05",
        "1982-04-05",
        "1983-04-05",
        "1984-04-04",
        "1985-04-05",
        "1986-04-05",
        "1987-04-05",
        "1988-04-04",
        "1989-04-05",
        "1990-04-05",
        "1991-04-05",
        "1992-04-04",
        "1993-04-05",
        "1994-04-05",
        "1995-04-05",
        "1996-04-04",
        "1997-04-05",
        "1998-04-05",
        "1999-04-05",
        "2000-04-04",
        "2001-04-05",
        "2002-04-05",
        "2003-04-05",
        "2004-04-04",
        "2005-04-05",
        "2006-04-05",
        "2007-04-05",
        "2008-04-04",
        "2009-04-04",
        "2010-04-05",
        "2011-04-05",
        "2012-04-04",
        "2013-04-04",
        "2014-04-05",
        "2015-04-05",
        "2016-04-04",
        "2017-04-04",
        "2018-04-05",
        "2019-04-05",
        "2020-04-04",
        "2021-04-04",
        "2022-04-05",
        "2023-04-05",
        "2024-04-04",
        "2025-04-04",
        "2026-04-05",
        "2027-04-05",
        "2028-04-04",
        "2029-04-04",
        "2030-04-05",
        "2031-04-05",
        "2032-04-04",
        "2033-04-04",
        "2034-04-05",
        "2035-04-05",
        "2036-04-04",
        "2037-04-04",
        "2038-04-05",
        "2039-04-05",
        "2040-04-04",
        "2041-04-04",
        "2042-04-04",
        "2043-04-05",
        "2044-04-04",
        "2045-04-04",
        "2046-04-04",
        "2047-04-05",
        "2048-04-04",
        "2049-04-04",
    ]
)

# Precomputed Buddha's Birthday dates on the Chinese Lunisolar Calendar.
# Also called Buddha Shakyamuni day
#
# See Also
# --------
# trading_calendars/etc/lunisolar china-buddhas-birthday
#
# Notes
# -----
# The holiday "Buddha's Birthday" is celebrated in many countries, though
# different calendars are used. This function is for Buddha's Birthday on
# the Chinese Lunisolar Calendar, where it is the 8th day of the 4th month.
chinese_buddhas_birthday_dates = pd.to_datetime(
    [
        "1959-05-15",
        "1960-05-03",
        "1961-05-22",
        "1962-05-11",
        "1963-05-01",
        "1964-05-19",
        "1965-05-08",
        "1966-05-27",
        "1967-05-16",
        "1968-05-04",
        "1969-05-23",
        "1970-05-12",
        "1971-05-02",
        "1972-05-20",
        "1973-05-10",
        "1974-04-29",
        "1975-05-18",
        "1976-05-06",
        "1977-05-25",
        "1978-05-14",
        "1979-05-03",
        "1980-05-21",
        "1981-05-11",
        "1982-05-01",
        "1983-05-20",
        "1984-05-08",
        "1985-05-27",
        "1986-05-16",
        "1987-05-05",
        "1988-05-23",
        "1989-05-12",
        "1990-05-02",
        "1991-05-21",
        "1992-05-10",
        "1993-05-28",
        "1994-05-18",
        "1995-05-07",
        "1996-05-24",
        "1997-05-14",
        "1998-05-03",
        "1999-05-22",
        "2000-05-11",
        "2001-04-30",
        "2002-05-19",
        "2003-05-08",
        "2004-05-26",
        "2005-05-15",
        "2006-05-05",
        "2007-05-24",
        "2008-05-12",
        "2009-05-02",
        "2010-05-21",
        "2011-05-10",
        "2012-04-28",
        "2013-05-17",
        "2014-05-06",
        "2015-05-25",
        "2016-05-14",
        "2017-05-03",
        "2018-05-22",
        "2019-05-12",
        "2020-04-30",
        "2021-05-19",
        "2022-05-08",
        "2023-05-26",
        "2024-05-15",
        "2025-05-05",
        "2026-05-24",
        "2027-05-13",
        "2028-05-02",
        "2029-05-20",
        "2030-05-09",
        "2031-05-28",
        "2032-05-16",
        "2033-05-06",
        "2034-04-26",
        "2035-05-15",
        "2036-05-03",
        "2037-05-22",
        "2038-05-11",
        "2039-04-30",
        "2040-05-18",
        "2041-05-07",
        "2042-05-26",
        "2043-05-16",
        "2044-05-05",
        "2045-05-24",
        "2046-05-13",
        "2047-05-02",
        "2048-05-20",
        "2049-05-09",
    ]
)

# Precomputed Dragon Boat (Tuen Ng Festival) dates.
# Also called "Duanwu"
#
# See Also
# --------
# trading_calendars/etc/lunisolar dragon-boat-festival
dragon_boat_festival_dates = pd.to_datetime(
    [
        "1960-05-29",
        "1961-06-17",
        "1962-06-06",
        "1963-06-25",
        "1964-06-14",
        "1965-06-04",
        "1966-06-23",
        "1967-06-12",
        "1968-05-31",
        "1969-06-19",
        "1970-06-08",
        "1971-05-28",
        "1972-06-15",
        "1973-06-05",
        "1974-06-24",
        "1975-06-14",
        "1976-06-02",
        "1977-06-21",
        "1978-06-10",
        "1979-05-30",
        "1980-06-17",
        "1981-06-06",
        "1982-06-25",
        "1983-06-15",
        "1984-06-04",
        "1985-06-22",
        "1986-06-11",
        "1987-06-01",
        "1988-06-18",
        "1989-06-08",
        "1990-05-28",
        "1991-06-16",
        "1992-06-05",
        "1993-06-24",
        "1994-06-13",
        "1995-06-02",
        "1996-06-20",
        "1997-06-09",
        "1998-05-30",
        "1999-06-18",
        "2000-06-06",
        "2001-06-25",
        "2002-06-15",
        "2003-06-04",
        "2004-06-22",
        "2005-06-11",
        "2006-05-31",
        "2007-06-19",
        "2008-06-08",
        "2009-05-28",
        "2010-06-16",
        "2011-06-06",
        "2012-06-23",
        "2013-06-12",
        "2014-06-02",
        "2015-06-20",
        "2016-06-09",
        "2017-05-30",
        "2018-06-18",
        "2019-06-07",
        "2020-06-25",
        "2021-06-14",
        "2022-06-03",
        "2023-06-22",
        "2024-06-10",
        "2025-05-31",
        "2026-06-19",
        "2027-06-09",
        "2028-05-28",
        "2029-06-16",
        "2030-06-05",
        "2031-06-24",
        "2032-06-12",
        "2033-06-01",
        "2034-05-22",
        "2035-06-10",
        "2036-05-30",
        "2037-06-18",
        "2038-06-07",
        "2039-05-27",
        "2040-06-14",
        "2041-06-03",
        "2042-06-22",
        "2043-06-11",
        "2044-05-31",
        "2045-06-19",
        "2046-06-08",
        "2047-05-29",
        "2048-06-15",
        "2049-06-04",
    ]
)


# Precomputed Day after the Mid-Autumn Festival
# Also called "Zhongqiu"
#
# See Also
# --------
# trading_calendars/etc/lunisolar mid-autumn-festival
mid_autumn_festival_dates = pd.to_datetime(
    [
        "1960-10-05",
        "1961-09-24",
        "1962-09-13",
        "1963-10-02",
        "1964-09-20",
        "1965-09-10",
        "1966-09-29",
        "1967-09-18",
        "1968-10-06",
        "1969-09-26",
        "1970-09-15",
        "1971-10-03",
        "1972-09-22",
        "1973-09-11",
        "1974-09-30",
        "1975-09-20",
        "1976-09-08",
        "1977-09-27",
        "1978-09-17",
        "1979-10-05",
        "1980-09-23",
        "1981-09-12",
        "1982-10-01",
        "1983-09-21",
        "1984-09-10",
        "1985-09-29",
        "1986-09-18",
        "1987-10-07",
        "1988-09-25",
        "1989-09-14",
        "1990-10-03",
        "1991-09-22",
        "1992-09-11",
        "1993-09-30",
        "1994-09-20",
        "1995-09-09",
        "1996-09-27",
        "1997-09-16",
        "1998-10-05",
        "1999-09-24",
        "2000-09-12",
        "2001-10-01",
        "2002-09-21",
        "2003-09-11",
        "2004-09-28",
        "2005-09-18",
        "2006-10-06",
        "2007-09-25",
        "2008-09-14",
        "2009-10-03",
        "2010-09-22",
        "2011-09-12",
        "2012-09-30",
        "2013-09-19",
        "2014-09-08",
        "2015-09-27",
        "2016-09-15",
        "2017-10-04",
        "2018-09-24",
        "2019-09-13",
        "2020-10-01",
        "2021-09-21",
        "2022-09-10",
        "2023-09-29",
        "2024-09-17",
        "2025-10-06",
        "2026-09-25",
        "2027-09-15",
        "2028-10-03",
        "2029-09-22",
        "2030-09-12",
        "2031-10-01",
        "2032-09-19",
        "2033-09-08",
        "2034-08-28",
        "2035-09-16",
        "2036-10-04",
        "2037-09-24",
        "2038-09-13",
        "2039-10-02",
        "2040-09-20",
        "2041-09-10",
        "2042-09-28",
        "2043-09-17",
        "2044-10-05",
        "2045-09-25",
        "2046-09-15",
        "2047-10-04",
        "2048-09-22",
        "2049-09-11",
    ]
)

# Precomputed Double Ninth Festival (Chung Yeung Festival) dates.
#
# See Also
# --------
# trading_calendars/etc/lunisolar double-ninth-festival
double_ninth_festival_dates = pd.to_datetime(
    [
        "1959-10-10",
        "1960-10-28",
        "1961-10-18",
        "1962-10-07",
        "1963-10-25",
        "1964-10-14",
        "1965-10-03",
        "1966-10-22",
        "1967-10-12",
        "1968-10-30",
        "1969-10-19",
        "1970-10-08",
        "1971-10-27",
        "1972-10-15",
        "1973-10-04",
        "1974-10-23",
        "1975-10-13",
        "1976-10-31",
        "1977-10-21",
        "1978-10-10",
        "1979-10-29",
        "1980-10-17",
        "1981-10-06",
        "1982-10-25",
        "1983-10-14",
        "1984-10-03",
        "1985-10-22",
        "1986-10-12",
        "1987-10-31",
        "1988-10-19",
        "1989-10-08",
        "1990-10-26",
        "1991-10-16",
        "1992-10-04",
        "1993-10-23",
        "1994-10-13",
        "1995-11-01",
        "1996-10-20",
        "1997-10-10",
        "1998-10-28",
        "1999-10-17",
        "2000-10-06",
        "2001-10-25",
        "2002-10-14",
        "2003-10-04",
        "2004-10-22",
        "2005-10-11",
        "2006-10-30",
        "2007-10-19",
        "2008-10-07",
        "2009-10-26",
        "2010-10-16",
        "2011-10-05",
        "2012-10-23",
        "2013-10-13",
        "2014-10-02",
        "2015-10-21",
        "2016-10-09",
        "2017-10-28",
        "2018-10-17",
        "2019-10-07",
        "2020-10-25",
        "2021-10-14",
        "2022-10-04",
        "2023-10-23",
        "2024-10-11",
        "2025-10-29",
        "2026-10-18",
        "2027-10-08",
        "2028-10-26",
        "2029-10-16",
        "2030-10-05",
        "2031-10-24",
        "2032-10-12",
        "2033-10-01",
        "2034-09-21",
        "2035-10-09",
        "2036-10-27",
        "2037-10-17",
        "2038-10-07",
        "2039-10-26",
        "2040-10-14",
        "2041-10-03",
        "2042-10-22",
        "2043-10-11",
        "2044-10-29",
        "2045-10-18",
        "2046-10-08",
        "2047-10-27",
        "2048-10-16",
        "2049-10-05",
    ]
)

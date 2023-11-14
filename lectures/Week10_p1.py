""" week10_slides_main.py

Main code for the simplified event study discussed in class

IMPORTANT: The simplified version of the event study includes the following
files

    toolkit/
    |   ...
    |__ webinars/
    |   |__ week10/
    |   |   |__ __init__.py
    |   |   |__ week10_slides_main.py       <- This module
    |   |   |__ week10_slides_data.py       <- Example data
    |   |__ lec_utils.py            <- Required
    |       ...


"""
import datetime as dt

import pandas as pd

from webinars import lec_utils as utils
from webinars.week10 import week10_slides_data as data

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = True


# ----------------------------------------------------------------------------
#   Step 2; Calculating returns
# ----------------------------------------------------------------------------
def step2(prc_csv, mkt_csv):
    """ Given CSV files with stock prices and market returns, create a data
    frame with stock and market returns


    Parameters
    ----------
    prc_csv: str, buffer
        Parameter to the passed to pd.read_csv. If string, it must be the
        location of a CSV file with prices downloaded from Yahoo Finance.

        The file must include the following columns:

        - date
        - close (column with close prices)

    mkt_csv: str, buffer
        Parameter to the passed to pd.read_csv. If string, it must be the
        location of a CSV file with market returns.

        The file must include the following columns:

        - date
        - mkt (column with market returns)

    Returns
    -------
    data frame:
        A data frame with stock returns (ret) and market returns (mkt). Index
        is a DatetimeIndex



    Notes
    -----

    Given two CSV files with the following data:

    prc_csv:

        | date       | open   | high   | low    | close  | adj_close |
        |------------+--------+--------+--------+--------+-----------|
        | 2020-09-18 | 447.94 | 451    | 428.8  | 442.15 | 442.15    |
        | 2020-09-21 | 453.13 | 455.68 | 407.07 | 449.39 | 449.39    |
        | 2020-09-22 | 429.6  | 437.76 | 417.6  | 424.23 | 424.23    |
        | 2020-09-23 | 405.16 | 412.15 | 375.88 | 380.36 | 380.36    |
        | 2020-09-24 | 363.8  | 399.5  | 351.3  | 387.79 | 387.79    |
        | 2020-09-25 | 393.47 | 408.73 | 391.3  | 407.34 | 407.34    |

    mkt_csv:

        | date       | mkt     |
        |------------+---------|
        | 2020-09-18 | -0.0088 |
        | 2020-09-21 | -0.0108 |
        | 2020-09-22 | 0.0102  |
        | 2020-09-23 | -0.0248 |
        | 2020-09-24 | 0.0025  |
        | 2020-09-25 | 0.0172  |

    This function will create the following DF:

                       mkt       ret
        date
        2020-09-21 -0.0108  0.016375
        2020-09-22  0.0102 -0.055987
        2020-09-23 -0.0248 -0.103411
        2020-09-24  0.0025  0.019534
        2020-09-25  0.0172  0.050414

        DatetimeIndex: 5 entries, 2020-09-21 to 2020-09-25
        Data columns (total 2 columns):
         #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   mkt     5 non-null      float64
         1   ret     5 non-null      float64

    """
    #   2.1: Load prices and mkt ret to data frames
    df = pd.read_csv(prc_csv, index_col='date', parse_dates=['date'])
    # utils.pprint(df, "df")

    mkt_df = pd.read_csv(mkt_csv, index_col='date', parse_dates=['date'])
    # utils.pprint(mkt_df, "mkt_df")

    #   2.2: Compute returns
    df.sort_index(inplace=True)

    df.loc[:, 'ret'] = df.loc[:, 'close'].pct_change()

    #   2.3: Join market returns
    df = df.join(mkt_df, how='inner')

    #   2.4: Keep only columns of interest
    cols = ['mkt', 'ret']
    df = df.loc[:, cols]

    # Get rid of any row with NaN
    df.dropna(inplace=True)

    return df.copy()


# ----------------------------------------------------------------------------
#  Step 3: Select the events of interest
# ----------------------------------------------------------------------------
def step3(rec_csv):
    """ Given a CSV file with the recommendations downloaded from Yahoo
    Finance, create a data frame with the events of interest.

    To select the events of interest:

    1. Keep only the last recommendation by a given firm on a given day
    2. Keep only upgrades and downgrades

    Create a column with the type of the event and a column with the event
    date.


    Parameters
    ----------
    rec_csv: str, buffer
        Parameter to the passed to pd.read_csv. If string, it must be the
        location of a CSV file with recommendations downloaded from Yahoo Finance.

        The file must include the following columns:

        - date
        - firm
        - action

    Returns
    -------
    frame:
        A data frame with the following columns:

        - firm (in upper case)
        - event_date (datetime)
        - event_type ("upgrade"/"downgrade")

        The index should be called event_id and start at 1

    Notes
    -----

    Given a CSV file with the following information:

      | date                | firm           | action   |
      |---------------------|----------------|----------|
      | 2012-02-16 07:42:00 | JP Morgan      | main     |
      | 2020-09-23 08:58:55 | Deutsche Bank  | main     | <-- Same firm/day
      | 2020-09-23 09:01:26 | Deutsche Bank  | main     | <-- Same firm/day
      | 2020-09-23 09:11:01 | Wunderlich     | down     |
      | 2020-09-23 11:15:12 | Deutsche bank  | up       | <-- Same firm/day
      | 2020-11-18 11:07:44 | Morgan Stanley | up       |
      | 2020-12-09 15:34:34 | JP Morgan      | main     |


    - Convert the values in "firm" to upper case
    - Create a column called "event_date" representing the date of the recommendation
    - Select the last observation for each firm-date
    - Create a column called event_type with values "upgrade" or "downgrade"
    - Keep only the relevant columns and replace the index with an event ID


    This function will return the DF:

                            firm  event_date event_type
        event_id
        1          DEUTSCHE BANK  2020-09-23    upgrade
        2             WUNDERLICH  2020-09-23  downgrade
        3         MORGAN STANLEY  2020-11-18    upgrade

        <class 'pandas.core.frame.DataFrame'>
        RangeIndex: 3 entries, 1 to 3
        Data columns (total 3 columns):
         #   Column      Non-Null Count  Dtype
        ---  ------      --------------  -----
         0   firm        3 non-null      object
         1   event_date  3 non-null      object
         2   event_type  3 non-null      object
        dtypes: object(3)

    """
    # Step 3.1. Read the appropriate CSV file with recommendations into a DF
    usecols = ['date', 'firm', 'action']
    df = pd.read_csv(rec_csv,
                     index_col='date',
                     parse_dates=['date'],
                     usecols=usecols)
    df.sort_index(inplace=True)

    # Step 3.2. Create variables identifying the firm and the event date
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    # Step 3.3. Deal with multiple recommendations
    groups = df.groupby(['event_date', 'firm'])
    # Select the last obs for each group using the GroupBy method `last`
    df = groups.last().reset_index()

    # Step 3.4. Create a table with all relevant events
    # 3.4.1: Subset the "action" column
    cond = df.loc[:, 'action'].str.contains('up|down')
    df = df.loc[cond]

    # 3.4.2: Create a column with the event type ("downgrade" or "upgrade")
    def _mk_et(value):
        """ Converts the string `value` as follows:
            - "down" --> "downgrade"
            - "up" --> "upgrade"
        and raise an exception if value is not "up" or "down"
        """
        if value == 'down':
            return 'downgrade'
        elif value == 'up':
            return 'upgrade'
        else:
            raise Exception(f'Unknown value for column `action`: {value}')

    df.loc[:, 'event_type'] = df.loc[:, 'action'].apply(_mk_et)

    # 3.4.3 Create the event id index:
    df.reset_index(inplace=True)
    df.index = df.index + 1
    df.index.name = 'event_id'

    # 3.4.4: Reorganise the columns
    cols = ['firm', 'event_date', 'event_type']
    df = df.loc[:, cols]

    return df.copy()


# ----------------------------------------------------------------------------
# Step 4: Calculate CARs for each event
#
# Overview:
#
# - Create the function `step4` (and auxiliary functions)
#
#     step4(ret_df, event_df) --> cars_df
#
# - The function `step4`:
#
#    - Applies the function `calc_car` to every row of `event_df`
#
#       calc_car(row of event_df, ret_df) --> scalar (CAR)
#
#    - The function `calc_car`
#
#       - Creates a data frame with "expanded" dates
#       - Join returns from `ret_df`
#       - Calculates the sum of abnormal returns (CAR)
#
# ----------------------------------------------------------------------------
def step4(ret_df, event_df):
    """ Calculate CARs for each event in `event_df`

    Parameters
    ----------
    ret_df : pandas dataframe
        A data frame with the following columns:
            ret : float
                Daily stock return
            mkt : float
                Daily market return
        The index is a DatetimeIndex corresponding to each trading day

        This data frame was created in step 2

    event_df : pandas dataframe
        A data frame with the events of interest (output of `step3`).

        Columns:
            firm : str
                The name of the firm issuing the recommendation
            event_date : str
                A string representing the date part of the recommendation,
                formatted as 'YYYY-MM-DD'.
            event_type : str
                A string identifying the event as either an upgrade
                ("upgrade") or downgrade ("downgrade")

        The index uniquely identifies each event (1, 2, ...)

    Returns
    -------
    data frame
        A data frame with the same format as `event_df` but with an additional
        column containing the CARs.

        Columns:
            firm : str
                The name of the firm issuing the recommendation
            event_date : str
                A string representing the date part of the recommendation,
                formatted as 'YYYY-MM-DD'.
            event_type : str
                A string identifying the event as either an upgrade
                ("upgrade") or downgrade ("downgrade")
            car : float
                The CAR for the two-day window surrounding the event
        Same index as `event_df`


    """
    cars = event_df.apply(calc_car, axis=1, ret_df=ret_df)
    event_df.loc[:, 'car'] = cars
    return event_df


# ----------------------------------------------------------------------------
#   Auxiliary functions
# ----------------------------------------------------------------------------
def expand_dates(ser):
    """ Given a row of `event_df`, returns a data frame with calendar dates
    for the event window [t-2, t+2]

    Parameters
    ----------
    ser : series
       Series corresponding to a row from the data frame produced by
        `mk_event_df`

    Returns
    -------
    df
        A Pandas data frame with the following structure:

        - df.index : Integers representing the ID of this event, that is,
            uniquely identifying a unique combination of values (<event_date>,
            <firm>). The index should start at 1.

        - df.columns : See Notes section below

    Notes
    -----

    """
    # Create a list of series
    ser_lst = [ser] * 5
    df = pd.concat(ser_lst, axis=1).transpose()

    # Replace the 'event_date' column with datetime
    ser = pd.to_datetime(df.loc[:, 'event_date'])
    df.drop(columns='event_date', inplace=True)
    df.loc[:, 'event_date'] = ser

    # Create the event time
    df.loc[:, 'event_time'] = [i for i in range(-2, 3)]

    # Create the return date
    df.loc[:, 'ret_date'] = df.event_date + pd.to_timedelta(df.event_time, unit='day')

    # keep only relevant columns
    cols = ['firm', 'event_date', 'event_time', 'ret_date']
    df = df.loc[:, cols]

    # rename the index
    df.index.name = 'event_id'
    return df


def calc_car(ser, ret_df):
    """ Given a row of event_df, compute cumulative abnormal returns
    for the event window from t-2 to t+2.

    Parameters
    ----------
    ser : series
       Series corresponding to a row from event_df

    ret_df : data frame
        A data frame with stock and market returns

    Returns
    -------
    float
        Cumulative abnormal return for this row

    """
    # Expand dates, set 'ret_date' as the new index, join rets
    # NOTE: I will create an auxiliary function to "expand" the dates for this
    # event
    dates = expand_dates(ser)
    dates.set_index('ret_date', inplace=True)
    df = dates.join(ret_df, how='inner')

    # Compute abnormal returns
    arets = df.loc[:, 'ret'] - df.loc[:, 'mkt']

    # Return the sum of aret but only if we have at least one obs
    if len(arets) > 0:
        return arets.sum()
    else:
        return None


# --------------------------------------------------------
#   Step 5: calculate t-stats
# --------------------------------------------------------
def step5(cars_df):
    """ Given a data frame with CARs and the event type for each event
    in the sample, compute a t-stat for each event type

    Parameters
    ----------
    cars_df : frame
        A data frame with CARs for each event (output of step3).
        This data frame must include the following columns:
        - event_type
        - car

    Returns
    -------
    frame:
        A data frame with the t-stat for each event type


    """

    # Separate between upgrades and downgrades
    groups = cars_df.groupby('event_type')['car']

    # Mean
    car_bar = groups.mean()

    # Standard error for mean (sem)
    car_sem = groups.sem()

    # t-stat
    # tstat = car_bar/car_sem

    # collect the number of obs in each group
    car_n = groups.count()

    # Construct the result data frame
    res = pd.DataFrame({'car_bar': car_bar, 'tstat': tstat, 'n_obs': car_n})
    return res


# ----------------------------------------------------------------------------
#   Main function
# ----------------------------------------------------------------------------
def main():
    """ Main function
    """

    # --------------------------------------------------------
    #   Step 1: Download data
    # --------------------------------------------------------
    # Instead of downloading the data, simply create "file-like" objects
    # containing the data in CSV-formatted strings
    #
    # These data match the example we discussed last week
    prc_csv = utils.csv_to_fobj(data.cnts_prc_csv)
    mkt_csv = utils.csv_to_fobj(data.cnts_mkt_csv)

    # Recommendations
    rec_csv = utils.csv_to_fobj(data.cnts_rec_csv)

    # --------------------------------------------------------
    #   Step 2: Calculate returns
    # --------------------------------------------------------
    ret_df = step2(prc_csv, mkt_csv)
    utils.pprint(ret_df, "ret_df")

    # --------------------------------------------------------
    #   Step 3: Events of interest
    # --------------------------------------------------------
    event_df = step3(rec_csv)
    utils.pprint(event_df, "event_df")

    # --------------------------------------------------------
    #   Step 4: Compute CARs
    # --------------------------------------------------------
    cars_df = step4(ret_df=ret_df, event_df=event_df)
    utils.pprint(cars_df, "cars_df")

    # --------------------------------------------------------
    #   Step 5: Calculate t-stats
    # --------------------------------------------------------
    # NOTE: instead of using the cars_df we created above, use
    # the cars_df created in the data module
    # res = step5(data.cars_df)
    # utils.pprint(res, "res")


if __name__ == "__main__":
    main()

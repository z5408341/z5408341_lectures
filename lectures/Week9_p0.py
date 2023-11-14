""" week9_slides_groups_and_bools.py

Codes discussed in class during Week 9

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ week9/
    |   |   |__ __init__.py                         <- Required (empty file)
    |   |   |__ week9_slides_groups_and_bools.py    <- This module
    |   |
    |   |__ lec_utils.py                        <- Required
    |       ...
    |__ toolkit_config.py


"""
import pandas as pd

from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False


# ----------------------------------------------------------------------------
#  Create the event data frame
# ----------------------------------------------------------------------------
def mk_rec_df0(show: bool = False):
    """ Creates an example DF

    Parameters
    ----------
    show: bool, optional
        If True, print DF

    Returns
    -------
    data frame :

                                     firm   action  event_date
        date
        2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
        2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
        2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
        2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
        2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
        2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 7 entries, 2012-02-16 07:42:00 to 2020-12-09 15:34:34
        Data columns (total 3 columns):
        #   Column      Non-Null Count  Dtype
        ---  ------      --------------  -----
        0   firm        7 non-null      object
        1   action      7 non-null      object
        2   event_date  7 non-null      object

    """
    cnts_rec_csv = '''
    date                , firm           , action
    2012-02-16 07:42:00 , JP Morgan      , main
    2020-09-23 08:58:55 , Deutsche Bank  , main
    2020-09-23 09:01:26 , Deutsche Bank  , main
    2020-09-23 09:11:01 , Wunderlich     , down
    2020-09-23 11:15:12 , Deutsche bank  , up
    2020-11-18 11:07:44 , Morgan Stanley , up
    2020-12-09 15:34:34 , JP Morgan      , main
    '''
    df = utils.csv_to_df(cnts_rec_csv, index_col='date', parse_dates=['date'])

    # Upper case version of 'firm' column
    df.loc[:, 'firm'] = df.loc[:, 'firm'].str.upper()

    # Create a string with the date part of the DatetimeIndex
    df.loc[:, 'event_date'] = df.index.strftime('%Y-%m-%d')

    if show is True:
        utils.pprint(df, "Example DF:")
    return df


def groupby_example0():
    """ Example illustrating groupby as a Slit-Apply-Combine operation

    In this example, we will split the DF into groups defined by the
    value of Firm
    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0(show=True)

    # Output:
    #
    # date                           firm action  event_date
    # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
    # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # Suppose we want to select the last rec for each firm (only)

    # Split into groups by firms

    # date                           firm action  event_date
    # 2012-02-16 07:42:00       JP MORGAN   main  2012-02-16
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # date                           firm action  event_date
    # 2020-09-23 08:58:55   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 09:01:26   DEUTSCHE BANK   main  2020-09-23
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

    # date                           firm action  event_date
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

    # date                           firm action  event_date
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Apply the operation "select last obs"

    # date                           firm action  event_date
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09

    # date                           firm action  event_date
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23

    # date                           firm action  event_date
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23

    # date                           firm action  event_date
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # Combine the result

    # date                           firm action  event_date
    # 2020-12-09 15:34:34       JP MORGAN   main  2020-12-09
    # 2020-09-23 11:15:12   DEUTSCHE BANK     up  2020-09-23
    # 2020-09-23 09:11:01      WUNDERLICH   down  2020-09-23
    # 2020-11-18 11:07:44  MORGAN STANLEY     up  2020-11-18

    # ----------------------------------------------------------------------------
    #   Creating groupby objects
    # ----------------------------------------------------------------------------
    groups = '?'
    # groups = df.groupby('firm')
    utils.pprint(groups, "df.groupby('firm')")

    # ----------------------------------------------------------------------------
    # The attribute "GroupBy.groups" -> Dict with groups
    # ----------------------------------------------------------------------------
    obj = '?'
    # groups = df.groupby('firm')
    # obj= groups.groups
    utils.pprint(obj, "groups.groups:", )

    # Output:
    # {'DEUTSCHE BANK': DatetimeIndex(['2020-09-23 08:58:55', '2020-09-23 09:01:26', '2020-09-23 11:15:12'],
    #                   dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'JP MORGAN': DatetimeIndex(['2012-02-16 07:42:00', '2020-12-09 15:34:34'],
    #                   dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'MORGAN STANLEY': DatetimeIndex([ '2020-11-18 11:07:44'],
    #                     dtype='datetime64[ns]', name='date', freq=None),
    #
    #  'WUNDERLICH': DatetimeIndex(['2020-09-23 09:11:01'],
    #                     dtype='datetime64[ns]', name='date', freq=None)
    #  }

    # ----------------------------------------------------------------------------
    #   The elements of groups.groups
    # ----------------------------------------------------------------------------
    # <example>
    # df = mk_rec_df0()
    # groups = df.groupby(by='firm')
    # for firm, idx in groups.groups.items():
    #    group_df = df.loc[idx]
    #    utils.pprint(group_df, msg=f"Data for Firm == '{firm}':", show_type=False)
    # </example>

    # ----------------------------------------------------------------------------
    #   Applying functions to individual groups
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    # <example>
    ## First, using a loop:
    ##
    ## Task: Create a dictionary with the number of observations
    ## for each value of "firm"
    # dic = {}
    # for firm, idx in groups.groups.items():
    #    nobs = len(df.loc[idx])
    #    print(f"Number of obs for Firm == '{firm}' is {nobs}")
    #    dic[firm] = nobs
    ##utils.pprint(dic, "This is dic:\n")
    # </example>

    # Then using the apply method
    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    res = '?'
    # res = groups.apply(len) # <mask>
    utils.pprint(res, "groups.apply(len):\n")

    # You can apply your own functions
    def get_last(df):
        """ Sorts the dataframe on its index and returns
            last row of the sorted dataframe
        """
        df.sort_index(inplace=True)
        return df.iloc[-1]

    df = mk_rec_df0()
    groups = df.groupby(by='firm')
    res = '?'
    # res = groups.apply(get_last) # <mask>
    utils.pprint(res, "groups.apply(get_last):\n")

    # Some group by operations are so common that Pandas implements them directly
    # on any created instance of `GroupBy`. Here are some examples:
    #
    # - `GroupBy.count`: count observations per group (exclude missing values)
    # - `GroupBy.size`: get group size, i.e., count observations per group (including missing values)
    # - `GroupBy.last`: select last of observation in each group

    # Count the number of observations inside each group:
    # (includes missing values if any)
    df = mk_rec_df0()
    groups = df.groupby('firm')
    res = '?'
    # res = groups.count()
    utils.pprint(res, "groups.count():\n")

    # Select last obs by group
    df = mk_rec_df0()
    groups = df.groupby('firm')
    res = '?'
    # res = df.groupby('firm').last() # <mark>
    utils.pprint(res, "df.groupby('firm').last():\n")


def groupby_example1():
    """ Grouping using multiple columns
    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    utils.pprint(df, "This is df:")

    # Split the data into groups
    groups = '?'
    # groups = df.groupby(['firm', 'event_date']) # <mask>
    utils.pprint(groups, "df.groupby(['firm', 'event_date']):\n")

    # Select the most recent obs for each group
    res = '?'
    # res = groups.last()
    utils.pprint(res, "groups.last():")

    # The index of the new DF is a MultiIndex
    obj = '?'
    # obj = res.index
    utils.pprint(obj, "The res.index:\n")

    # Converting the index to columns

    # <example>
    # df = mk_rec_df0()
    # df.sort_index(inplace=True)
    # groups = df.groupby(['firm', 'event_date'])
    # res = groups.last()
    # utils.pprint(res,  "res:\n")
    # new_df = res.reset_index()
    # utils.pprint(new_df,  "res.reset_index():\n")
    # </example>


# ----------------------------------------------------------------------------
#   New topic: Selecting using booleans
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
#   New example DF
# ----------------------------------------------------------------------------
def mk_rec_df1():
    """ Creates an example DF

    Returns
    -------
    data frame :

         event_date            firm action
      0  2012-02-16       JP MORGAN   main
      1  2020-09-23   DEUTSCHE BANK     up
      2  2020-09-23      WUNDERLICH   down
      3  2020-11-18  MORGAN STANLEY     up
      4  2020-12-09       JP MORGAN   main

      <class 'pandas.core.frame.DataFrame'>
      RangeIndex: 5 entries, 0 to 4
      Data columns (total 3 columns):
       #   Column      Non-Null Count  Dtype
      ---  ------      --------------  -----
       0   event_date  5 non-null      object
       1   firm        5 non-null      object
       2   action      5 non-null      object

    """
    # --------------------------------------------------------
    # Start with the example df and keep only the last rec
    # by a given firm on a given day
    # --------------------------------------------------------
    df = mk_rec_df0()
    df.sort_index(inplace=True)
    groups = df.groupby(['event_date', 'firm'])
    df = groups.last().reset_index()
    return df


def bool_example0():
    """ Given a DF with the last rec for each firm/event-day, keep only
    upgrades and downgrades

    """
    # ----------------------------------------------------------------------------
    #   Creates the example data frame
    # ----------------------------------------------------------------------------
    df = mk_rec_df1()
    utils.pprint(df, "This is df:\n")

    # ----------------------------------------------------------------------------
    #   Using booleans to select rows
    # ----------------------------------------------------------------------------
    # will be a series with boolean values
    cond = '?'
    # cond = df.loc[:, 'action'] == 'up'
    utils.pprint(cond, "cond = df.loc[:, 'action'] == 'up'\nThen cond is:\n")

    # We can use this series as an indexer:
    # A series of booleans can be used to select rows that meet the criteria
    res = '?'
    # res = df.loc[cond] # <mask>
    utils.pprint(res, "df.loc[cond]:\n")

    # ----------------------------------------------------------------------------
    #   Using booleans to select rows and cols
    # ----------------------------------------------------------------------------
    col_cond = [False, True, False]
    res = '?'
    # res = df.loc[:, col_cond] # <mask>
    # utils.pprint(df, "This is df:\n")
    utils.pprint(res, f"The output of df.loc[:, {col_cond}] is:\n")

    # ----------------------------------------------------------------------------
    #   Multiple criteria
    # ----------------------------------------------------------------------------
    # Combine different criteria
    res = '?'
    # crit = (df.loc[:, 'action'] == 'up') | (df.loc[:, 'action'] == 'down')
    # res = df.loc[crit]
    utils.pprint(res, "df.loc[crit]")

    # ----------------------------------------------------------------------------
    #   Using the `str.contains` method
    # ----------------------------------------------------------------------------
    crit = '?'
    # crit = df.loc[:, 'action'].str.contains('up|down') # <mask>
    # res = df.loc[crit]
    utils.pprint(res, "df.loc[:, 'action'].str.contains('up|down'):\n")


def mk_event_df0():
    """ Example showing how to create the column "event_type"
    This is df:

    Given the following DF

       event_date            firm action
    1  2020-09-23   DEUTSCHE BANK     up
    2  2020-09-23      WUNDERLICH   down
    3  2020-11-18  MORGAN STANLEY     up

    This example produces:

                        firm  event_date event_type
    event_id
    1          DEUTSCHE BANK  2020-09-23    upgrade
    2             WUNDERLICH  2020-09-23  downgrade
    3         MORGAN STANLEY  2020-11-18    upgrade

    """
    # Start with the recs and keep only upgrades/downgrades
    df = mk_rec_df1()
    crit = df.loc[:, 'action'].str.contains('up|down')  # <mask>
    df = df.loc[crit]
    utils.pprint(df, "This is df:\n")

    # ----------------------------------------------------------------------------
    #  Create a column called event_type
    # ----------------------------------------------------------------------------
    event_df = df.copy()

    def _et(value):
        if value == 'up':
            return 'upgrade'
        elif value == 'down':
            return 'downgrade'
        else:
            raise Exception(f"value must be either 'up' or 'down'")

    event_df.loc[:, 'event_type'] = event_df.loc[:, 'action'].apply(_et)
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>

    # ----------------------------------------------------------------------------
    #  Keep only the columns of interest
    # ----------------------------------------------------------------------------
    cols = ['firm', 'event_date', 'event_type']
    event_df = event_df.loc[:, cols]
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>

    # ----------------------------------------------------------------------------
    #  Add the index
    # ----------------------------------------------------------------------------
    event_df.reset_index(inplace=True, drop=True)
    event_df.index = event_df.index + 1
    event_df.index.name = 'event_id'
    # <example>
    # utils.pprint(event_df, "event_df:")
    # </example>
    return event_df


def apply_example0():
    """ How to use the data frame method apply
    """
    # Example DF
    df = mk_event_df0()
    df.loc[:, 'event_type'] = df.event_type.str.upper()
    utils.pprint(df, "df:")

    # apply
    res = df.apply(max)
    utils.pprint(res, "df.apply(max)")

    # what if we want "row-wise"?

    res = df.apply(max, axis=1)
    utils.pprint(res, "df.apply(max, axis=1)")

    def sel_lower(ser, pos):
        """ Replace the element at position `pos` with lowercase
        """
        ser.iloc[pos] = ser.iloc[pos].lower()
        return ser

    res = df.apply(sel_lower, pos=0)
    utils.pprint(res, "df.apply(sel_lower, pos=0)")


if __name__ == "__main__":
    # Example DF
    # df = mk_rec_df0(show=True)

    # groupby_example0()
    # groupby_example1()

    # bool_example0()
    # mk_event_df0()

    # apply_example0()

    pass

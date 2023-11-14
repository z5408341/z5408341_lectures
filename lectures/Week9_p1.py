""" week9_slides_joins.py

Codes discussed in class during Week 9

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ week9/
    |   |   |__ __init__.py             <- Required (empty file)
    |   |   |__ lec_utils.py            <- Required
    |   |   |__ week9_slides_joins.py   <- This module
    |       ...
    |__ toolkit_config.py


"""
import textwrap

import pandas as pd

from webinars import lec_utils as utils

utils.pp_cfg.sep = True
utils.pp_cfg.df_info = False


# Aux function
def _join_msg(msg):
    """ format msg for the join examples
    """
    return textwrap.dedent(msg)


# ----------------------------------------------------------------------------
#   Joins
# ----------------------------------------------------------------------------
def example_joins():
    """ Example illustrating the following types of joins

    - left
    - right
    - outer
    - inner

    In all cases, the goal is to join a table called "Left" to a table called "Right"
    The result will be a table called "Merged"

     Left:                         Right:                  Merged

     | idx | L  |   Join type      | idx | R  |  Result   | idx | L   | R   |
     |-----|----|                  |-----|----|           |-----|-----|-----|
     | 1   | L1 |   ----------->   | 3   | R3 |  -------> | ... | ... | ... |
     | 2   | L2 |                  | 4   | R4 |           | ... | ... | ... |
     | 3   | L3 |                  | 5   | R5 |


    """
    # Create two data frames:
    #
    # Left:
    #
    # | idx | L  |
    # |-----+----|
    # | 1   | L1 |
    # | 2   | L2 |
    # | 3   | L3 |
    left_cnts = '''
        idx , L  
        1   , L1 
        2   , L2 
        3   , L3 
        '''
    left = '?'
    left = utils.csv_to_df(left_cnts, index_col='idx')  # <mask>
    utils.pprint(left, "This is left:")

    # Right:
    #
    # | idx | R  |
    # |-----+----|
    # | 3   | R3 |
    # | 4   | R4 |
    # | 5   | R5 |
    right_cnts = '''
        idx , R  
        3   , R3 
        4   , R4 
        5   , R5 
        '''
    right = '?'
    right = utils.csv_to_df(right_cnts, index_col='idx')  # <mask>
    utils.pprint(right, "This is right:")

    # In general:
    #
    # Left:                        Right:                   Merged
    #
    # | idx | L  | Join type    | idx | R  | Result   | idx | L   | R   |
    # | 1   | L1 | -----------> | 3   | R3 | -------> | ... | ... | ... |
    # | 2   | L2 |              | 4   | R4 |          | ... | ... | ... |
    # | 3   | L3 |              | 5   | R5 |
    #
    # The resulting table will depend on the type of join:

    msg = '''
    Left join: Keep all the idxs of the left table (Left)

    Left:                       Right:                 Merged

    | idx | L  |   Left Join   | idx | R  |  Result   |idx| L  |  R  |
    | 1   | L1 |  -----------> | 3   | R3 |  -------> |1  | L1 | NaN |
    | 2   | L2 |               | 4   | R4 |           |2  | L2 | NaN |
    | 3   | L3 |               | 5   | R5 |           |3  | L3 |  R3 |

    '''
    #
    res = '?'
    # res = left.join(right, how='left') # <mask>
    utils.pprint(res, _join_msg(msg))

    msg = '''
    Right join: Keep all the idxs of the right table (Right)

    Left:                       Right:                  Merged

    | idx | L  | Right Join   | idx | R  | Result   | idx | L   | R  |
    | 1   | L1 | -----------> | 3   | R3 | -------> | 3   | L3  | R3 |
    | 2   | L2 |              | 4   | R4 |          | 4   | NaN | R4 |
    | 3   | L3 |              | 5   | R5 |          | 5   | NaN | R5 |
    '''

    res = '?'
    # res = left.join(right, how='right') # <mask>
    utils.pprint(res, _join_msg(msg))

    msg = '''
    Inner join: Keep only the idxs that exist in both left and right

    Left:                     Right:              Merged

    |idx| L |  Inner Join   |idx| R |  Result   |idx| L | R |
    |1  | L1|  -----------> |3  | R3|  -------> |3  | L3| R3|
    |2  | L2|               |4  | R4|           
    |3  | L3|               |5  | R5|           
    '''

    res = '?'
    # res = left.join(right, how='inner') # <mask>
    utils.pprint(res, _join_msg(msg))

    msg = '''
    Outer join: Keep all the idxs in left and right

     Left:                   Right:              Merged

    |idx| L |  Outer Join   |idx| R |  Result   |idx| L | R |
    |1  | L1|  -----------> |3  | R3|  -------> |1  | L1|NaN|
    |2  | L2|               |4  | R4|           |2  | L2|NaN|
    |3  | L3|               |5  | R5|           |3  | L3| R3|
                                                |4  |NaN| R4|
                                                |5  |NaN| R5|
    '''
    res = '?'
    # res = left.join(right, how='outer') # <mask>
    utils.pprint(res, _join_msg(msg))


def example_df_plus_obj():
    """ Example showing how to add pandas objects aligned by index
    """
    # Create two data frames:
    #
    # base
    #
    # | idx | L  | R  |
    # |-----+----|----|
    # | 1   | 11 | 12 |
    # | 2   | 21 | 22 |
    # | 3   | 31 | 32 |
    cnts = '''
        idx , L  , R  
        1   , 11 , 12 
        2   , 21 , 22 
        3   , 31 , 32 
        '''
    base = utils.csv_to_df(cnts, index_col='idx')
    utils.pprint(base, "This is base:")

    # Other DF:
    #
    # | idx | R  |
    # |-----+----|
    # | 3   | 3  |
    # | 4   | 4  |
    # | 5   | 5  |
    cnts = '''
        idx , R  
        3   , 3 
        4   , 4 
        5   , 5 
        '''
    other_df = utils.csv_to_df(cnts, index_col='idx')
    utils.pprint(other_df, "The other_df:")

    # Pandas will align indexes and columns (as if outer join)
    res = '?'
    # res = base + other_df  # <mask>
    utils.pprint(res, "base + other_df:")

    # df + series is different (align column index)
    res = '?'
    # res = base + other_df.loc[:, 'R'] # <mask>
    utils.pprint(res, "base + other_df.loc[:, 'R']:")


def example_ret_and_mkts():
    """ Combining stock and market returns
    """
    cnts_mkt_csv = '''
        date       , mkt
        2020-09-18 , -0.0088
        2020-09-21 , -0.0108
        2020-09-22 , 0.0102
        2020-09-23 , -0.0248
        2020-09-24 , 0.0025
        2020-09-25 , 0.0172
        '''
    df_mkt = utils.csv_to_df(cnts_mkt_csv, index_col='date', parse_dates=['date'])
    utils.pprint(df_mkt, "This is df_mkt:")

    cnts_ret_csv = '''
        date       ,   ret
        2020-09-21 , 0.016375
        2020-09-22 ,-0.055987
        2020-09-23 ,-0.103411
        2020-09-24 , 0.019534
        2020-09-25 , 0.050414
        '''
    df_ret = utils.csv_to_df(cnts_ret_csv, index_col='date', parse_dates=['date'])
    utils.pprint(df_ret, "This is df_ret:")

    combined = '?'
    # combined = df_ret.join(df_mkt, how='inner')
    utils.pprint(combined, "This is combined:")


if __name__ == "__main__":
    pass
    # example_joins()
    # example_df_plus_obj()
    # example_ret_and_mkts()

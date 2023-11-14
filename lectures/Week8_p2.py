""" week7_slides_p2.py

Codes discussed in class during Week 8, Part 2: Time series with Pandas

IMPORTANT: This code requires the lec_utils module (available in dropbox)

    toolkit/
    |   ...
    |__ webinars/
    |   |__ __init__.py             <- Required (empty file)
    |   |__ lec_utils.py            <- Required
    |   |
    |   |__ week8/
    |   |   |__ __init__.py             <- Required (empty file)
    |   |   |__ week8_slides_p1.py
    |   |   |__ week8_slides_p2.py      <- This module
    |       ...
    |__ toolkit_config.py

I will talk about the `lec_utils.py` module during class

"""
import os
import datetime as dt

import pandas as pd

from webinars import lec_utils as utils
import toolkit_config as cfg

# Set the options for this part of the lecture
# (all this does is to modify the behavior of pprint)
utils.pp_cfg.sep = True
utils.pp_cfg.df_info = True
utils.pp_cfg.df_max_rows = 100
utils.pp_cfg.df_max_cols = 10

# ----------------------------------------------------------------------------
#   Review (Week 7):
#   The pandas.read_csv function
# ----------------------------------------------------------------------------
# Source file:
QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')

# Reading the content of a file
# <example>
#df0 = pd.read_csv(QAN_PRC_CSV, index_col='Date')
#utils.pprint(df0, "df0")
# </example>


# ----------------------------------------------------------------------------
# Problem: Working with CSV files not ideal to create examples during class
# Solution: Use str formatted as CSV
#
# The variable `csv_cnts` will point to a str instance whose value looks
# like the contents of a CSV file (think of it as a "fake" csv file)
# ----------------------------------------------------------------------------
csv_cnts = '''
date       , open   , high   , low    , close  , volume
2010-06-29 , 3.80   , 5.00   , 3.51   , 4.78   , 93831500
2010-06-30 , 5.16   , 6.08   , 4.66   , 4.77   , 85935500
2010-07-01 , 5.00   , 5.18   , 4.05   , 4.39   , 41094000
2010-07-02 , 4.60   , 4.62   , 3.74   , 3.84   , 25699000
2010-07-06 , 4.00   , 4.00   , 3.17   , 3.22   , 34334500
2010-07-07 , 3.27   , 3.32   , 2.99   , 3.16   , 34608500
2010-07-08 , 3.22   , 3.50   , 3.11   , 3.49   , 38557000
2010-07-09 , 3.51   , 3.57   , 3.30   , 3.48   , 20253000
2010-07-12 , 3.58   , 3.61   , 3.40   , 3.41   , 11012500
2010-07-13 , 3.47   , 3.72   , 3.38   , 3.62   , 13400500
2020-11-02 , 394.00 , 406.98 , 392.30 , 400.51 , 29021100
2020-11-03 , 409.73 , 427.77 , 406.69 , 423.90 , 34351700
2020-11-04 , 430.62 , 435.40 , 417.10 , 420.98 , 32143100
2020-11-05 , 428.30 , 440.00 , 424.00 , 438.09 , 28414500
2020-11-06 , 436.10 , 436.57 , 424.28 , 429.95 , 21706000
2020-12-23 , 632.20 , 651.50 , 622.57 , 645.98 , 33173000
2020-12-24 , 642.99 , 666.09 , 641.00 , 661.77 , 22865600
2020-12-28 , 674.51 , 681.40 , 660.80 , 663.69 , 32278600
2020-12-29 , 661.00 , 669.90 , 655.00 , 665.99 , 22910800
'''

# We could try to create a DF with the str above
#
# Problem: Pandas will generate an exception because it expects a file obj
# (or a str representing the location of a file)
#
# pd.read_csv does work here...
#
# <example>
#df = pd.read_csv(csv_cnts) # -> Exception
# </example>


# Solution: We can convert the str above to something that behaves like
# a file object
#
#  lec_utils.csv_to_fobj(str) -> file object
#

# <example>
#tsla_prc_csv = utils.csv_to_fobj(csv_cnts)
#df = pd.read_csv(tsla_prc_csv) # -> DF
#utils.pprint(df, "pd.read_csv(tsla_prc_cv")
# </example>


# Alternatively: lec_utils.csv_to_df(str) -> DF
# <example>
#df = utils.csv_to_df(csv_cnts)
#utils.pprint(df)
# </example>

# ----------------------------------------------------------------------------
#   Time series with Pandas
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
#   Load the data in csv_cnts into a dataframe
# ----------------------------------------------------------------------------
# df will be:
#             date    open    high     low   close     volume
#   0   2010-06-29    3.80    5.00    3.51    4.78   93831500
#   1   2010-06-30    5.16    6.08    4.66    4.77   85935500
#   2   2010-07-01    5.00    5.18    4.05    4.39   41094000
#   3   2010-07-02    4.60    4.62    3.74    3.84   25699000
#   4   2010-07-06    4.00    4.00    3.17    3.22   34334500
#   5   2010-07-07    3.27    3.32    2.99    3.16   34608500
#   6   2010-07-08    3.22    3.50    3.11    3.49   38557000
#   7   2010-07-09    3.51    3.57    3.30    3.48   20253000
#   8   2010-07-12    3.58    3.61    3.40    3.41   11012500
#   9   2010-07-13    3.47    3.72    3.38    3.62   13400500
#   10  2020-11-02  394.00  406.98  392.30  400.51   29021100
#   11  2020-11-03  409.73  427.77  406.69  423.90   34351700
#   12  2020-11-04  430.62  435.40  417.10  420.98   32143100
#   13  2020-11-05  428.30  440.00  424.00  438.09   28414500
#   14  2020-11-06  436.10  436.57  424.28  429.95   21706000
#   15  2020-12-23  632.20  651.50  622.57  645.98   33173000
#   16  2020-12-24  642.99  666.09  641.00  661.77   22865600
#   17  2020-12-28  674.51  681.40  660.80  663.69   32278600
#   18  2020-12-29  661.00  669.90  655.00  665.99   22910800
#
#   <class 'pandas.core.frame.DataFrame'>
#   RangeIndex: 19 entries, 0 to 18
#   Data columns (total 7 columns):
#    #   Column     Non-Null Count  Dtype
#   ---  ------     --------------  -----
#    0   date       19 non-null     object
#    1   open       19 non-null     float64
#    2   high       19 non-null     float64
#    3   low        19 non-null     float64
#    4   close      19 non-null     float64
#    6   volume     19 non-null     int64
#   dtypes: float64(5), int64(1), object(1)
#   memory usage: 1.2+ KB

df  = '?'

#df = pd.read_csv(csv_cnts)

# But this will:

# <example>
#tsla_prc_csv = utils.csv_to_fobj(csv_cnts)
#df = pd.read_csv(tsla_prc_csv)
#utils.pprint(df, "This is df:")
# </example>


# 'date' is a column of strings representing dates.

# <example>
#res = df.loc[:, 'date']
#utils.pprint(res, "df.loc[:, 'date'] gives:")
# </example>

# The index is just a counter (RangeIndex)
#utils.pprint(df.index, "df.index gives:")

# ----------------------------------------------------------------------------
# How can we convert the strings in 'date' to datetime objects?
#
# The `pandas.to_datetime` method:
#   - converts strings representing dates into datetime and returns a pandas object
#     with the result.
#
#   - You can specify the string format using the same arguments as
#     datetime.strftime
#
#   - If you do not specify the format, pandas will guess.
# ----------------------------------------------------------------------------

# strftime format for the dates above is:
fmt = '%Y-%m-%d'

# Important: When the obj in pd.to_datetime(obj) is a series, Pandas will
# return another series with datetime objects

# <example>
#date_ser = df.loc[:, 'date'] # This is a series
#dt_ser = pd.to_datetime(date_ser, format=fmt)
#utils.pprint(date_ser, "df.loc[:, 'date'] is:")
#utils.pprint(dt_ser, "Converting to datetime using `pd.to_datetime` gives:")
# </example>


# We can use assignment statements to convert columns
#
# Convert the elements in the Date column
df.loc[:, 'date']  = '?'
#df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])


#utils.pprint(df, "DF after converting date column")


# ----------------------------------------------------------------------------
#   Setting the index
# ----------------------------------------------------------------------------
# We can set the index to a column containing datetime objects

# <example>
#df = utils.csv_to_df(csv_cnts)
#df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])
#utils.pprint(df, "DF before setting the index")
#df.set_index('date', inplace=True)
#utils.pprint(df, "DF after setting the index")
#utils.pprint(df.index)
# </example>


# ----------------------------------------------------------------------------
#   Setting datetime indexes during read_csv
# ----------------------------------------------------------------------------
# previously:

# <example>
#tsla_prc_csv = utils.csv_to_fobj(csv_cnts)
#df = pd.read_csv(tsla_prc_csv)
#df.loc[:, 'date'] = pd.to_datetime(df.loc[:, 'date'])
#df.set_index('date', inplace=True)
# </example>

# New version
# <example>
## We must "create a new fake CSV file" first
#tsla_prc_csv = utils.csv_to_fobj(csv_cnts)
#df = pd.read_csv(tsla_prc_csv, parse_dates=['date'], index_col='date')
#utils.pprint(df)
# </example>

# Even better, the lec_utils.csv_to_df takes the same parameters as pd.read_csv
# <example>
## Note that csv_cnts is a string, not an fobj
#df = utils.csv_to_df(csv_cnts, parse_dates=['date'], index_col='date')
#utils.pprint(df)
# </example>

# ----------------------------------------------------------------------------
#   Illustrating the advantages of a datetime indexes
# ----------------------------------------------------------------------------
# Select all data for a given year in one go
df_2020  = '?'
#df_2020 = df.loc['2020']


utils.pprint(df_2020)

# Select all data for a given month
df_2020_11  = '?'
#df_2020_11 = df.loc['2020-11'] # <mask>


utils.pprint(df_2020_11)

# Selecting date ranges using strings
df_2020_11_0204  = '?'
#df_2020_11_0204 = df.loc['2020-11-02':'2020-11-04']
#utils.pprint(df_2020_11_0204)


# ----------------------------------------------------------------------------
# Computing returns
#   - Make sure the data frame is sorted!
#   - Make sure you know how pandas will tread missing values
# ----------------------------------------------------------------------------
# Make sure the dataframe is sorted

# <example>
#df = utils.csv_to_df(csv_cnts, index_col='date', parse_dates=['date'])
#df.sort_index(inplace=True)
## Note that pandas will use the previous date (whatever that is, by default)
#rets = df.loc[:, 'close'].pct_change()  # <mask>
#utils.pprint(rets)
# </example>


# You can specify the frequency pandas will use to computer returns.
# freq='B' will compute returns using consecutive business days
# (problem: does not deal with holidays)

# <example>
#rets = df.loc[:, 'close'].pct_change(freq='B')  # <mask>
#utils.pprint(rets)
# </example>

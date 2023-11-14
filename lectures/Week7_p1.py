import pprint as pp

import pandas as pd



def printit(obj, msg=None):

    sep = '-' * 40
    if isinstance(obj, str) and obj == '?':
        return None
    elif isinstance(obj, str):
        prt = obj
    elif isinstance(obj, (pd.DataFrame, pd.Series)):
        prt = obj.to_string()
    else:
        prt = pp.pformat(obj)
    if not isinstance(obj, str):
        prt = f'{prt}\n\nType: {type(obj)}'
    if msg is not None:
        prt = f'{msg}\n\n{prt}'
    to_print = [
        '',
        sep,
        prt,
        sep,
    ]
    print('\n'.join(to_print))


dates = [
    '2020-01-02',
    '2020-01-03',
    '2020-01-06',
    '2020-01-07',
    '2020-01-08',
    '2020-01-09',
    '2020-01-10',
    '2020-01-13',
    '2020-01-14',
    '2020-01-15',
]
prices = [
    7.1600,
    7.1900,
    7.0000,
    7.1000,
    6.8600,
    6.9500,
    7.0000,
    7.0200,
    7.1100,
    7.0400,
]
# Trading day counter
bday = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10]

# ----------------------------------------------------------------------------
#   Create instances
# ----------------------------------------------------------------------------
# Create a series object
ser = pd.Series(data=prices, index=dates)
# printit(ser, "The series `ser`:")

# ----------------------------------------------------------------------------
#   the series look like this:
# ----------------------------------------------------------------------------
# ser:
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04


# Data Frame with close and Bday columns
df = pd.DataFrame(data={'close': ser, 'bday': bday}, index=dates)
# printit(df, "The data frame `df`:")

# ----------------------------------------------------------------------------
#   The DF looks like this
# ----------------------------------------------------------------------------
# df:
#               close  bday
#   2020-01-02   7.16     1
#   2020-01-03   7.19     2
#   2020-01-06   7.00     3
#   2020-01-07   7.10     4
#   2020-01-08   6.86     5
#   2020-01-09   6.95     6
#   2020-01-10   7.00     7
#   2020-01-13   7.02     8
#   2020-01-14   7.11     9
#   2020-01-15   7.04    10


# ----------------------------------------------------------------------------
#   Selection using Series
#   1. Use ser.loc to select using labels
#       1.1. Single label
#       1.2. List of labels
#       1.2. Slice of labels
#   2. Use ser.iloc to select using position (integers)
#       2.1. Single integer
#       2.2. List integers
#       2.2. Slice of integers
# ----------------------------------------------------------------------------


# ------------------------------------------------------------
# Series.loc: Selection using a single label
# ser.loc[label] --> scalar if label in index, error otherwise
# ------------------------------------------------------------
# Task: Select the element with label '2020-01-10':
#
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00 <--
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The result will be 7.00

label = '2020-01-10'
res = '?'
# res = ser.loc[label]

printit(res, f"ser.loc[{label}]:")

# IMPORTANT: Label must exist in the index
label = '2020-01-30'
# <example>
# res = ser.loc[label] # --> KeyError
# </example>


# ------------------------------------------------------------
# Series.loc: Selection using a sequence of labels
# ser.loc[seq] --> series if labels in index, error otherwise
# ------------------------------------------------------------
# Task: Select the following elements from `ser`
#
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00 <--
#   2020-01-13    7.02 <--
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The result will be the series:
#   2020-01-10    7.00
#   2020-01-13    7.02

label_seq = ['2020-01-10', '2020-01-13']
res = '?'
# res = ser.loc[label_seq]

printit(res, f"ser.loc[{label_seq}]")

# NOTE: Every label must exist
label_seq = ['2020-01-10', '2020-01-11']
# <example>
# res = ser.loc[label_seq] # --> KeyError
# </example>


# ------------------------------------------------------------
# Series.loc: Selection using slices
# ser.loc[slice] --> series
# ------------------------------------------------------------
# Task: Select the following elements from the series using slices
#
#   2020-01-02    7.16
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00 <--
#   2020-01-13    7.02 <--
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The output will be a series:
#
#   2020-01-10    7.00  <--
#   2020-01-13    7.02  <--

# When using slices, Pandas will return the **interval** of labels that
# included in the slice
#
# IMPORTANT: ENDPOINTS ARE INCLUDED!!!
start = '2020-01-10'
end = '2020-01-13'
res = '?'
# res = ser.loc[start:end]

printit(res, f"ser.loc['{start}':'{end}']")

# Be careful when using slices: For instance suppose you made a mistake
# and set the start of the slice to '3020-01-10' (i.e., 3020 instead of 2020)
#
# Pandas will try to find the interval of index labels that is included in a
# slice that that starts with '3020-01-10'. There is no such slice, so the
# result will be an empty series

start = '3020-01-10'
end = '2020-01-13'
res = '?'
# res = ser.loc[start:end]

printit(res, f"ser.loc['{start}':'{end}']")

# IMPORTANT: Selection using slices will NOT GENERATE ERRORS as long as the labels
# data type is consistent with the index. For instance, the following slice
# does not make logical sense.
#
#   start = 'start'
#   end = 'end'
#
# Pandas will try to find the interval of index labels that begins with
# "start". Since the letter "s" comes after the number "2" (in alphabetical
# order), the interval of index labels is empty:
start = 'start'
end = 'end'
res = '?'
# res = ser.loc[start:end]

printit(res, f"ser.loc['{start}':'{end}']")

# ------------------------------------------------------------
# ser.loc can be used in assignemnt statements:
# <target> = <expression>
# ------------------------------------------------------------
# Task: Suppose we want to set the value of the element with
# label '2020-01-10' to -99
#
#                   |
#                   V
#   2020-01-02     7.16
#   2020-01-03     7.19
#   2020-01-06     7.00
#   2020-01-07     7.10
#   2020-01-08     6.86
#   2020-01-09     6.95
#   2020-01-10   -99.00     <--
#   2020-01-13     7.02
#   2020-01-14     7.11
#   2020-01-15     7.04

# First, we will create a copy of the original series
# NOTE: You can create  copies of both series and data frames using the
# method .copy
#
# The following statement will create a NEW series with the same data and
# indexes as the one assigned to the variable `ser`:
ser2 = ser.copy()

# <example>
# old_label = '2020-01-10' # NOTE: This label exists in the index
# ser2.loc[old_label] = -99
# printit(ser2, f"The ser2:")
# </example>

# Task: Suppose we want to add a new element to the series with
# label '2020-01-11' and value -99
#
#                   |
#                   V
#   2020-01-02     7.16
#   2020-01-03     7.19
#   2020-01-06     7.00
#   2020-01-07     7.10
#   2020-01-08     6.86
#   2020-01-09     6.95
#   2020-01-10     7.00
#   2020-01-11     -99      <-- New
#   2020-01-13     7.02
#   2020-01-14     7.11
#   2020-01-15     7.04

# First try: Just use an assignment statement
# <example>
# new_label = '2020-01-11' # NOTE: This label does not exist
# ser2.loc[new_label] = -99
# printit(ser2, f"The new ser2:")
# </example>

# If what we did above was enough, the expression
#
#   ser2.loc['2020-01-10':'2020-01-13']
#
# should return:
#
#   2020-01-10     7.00
#   2020-01-11     -99
#   2020-01-13     7.02
#
# However, this is NOT the case

# <example>
# start = '2020-01-10'
# end = '2020-01-13'
# res = ser2.loc[start:end]
# printit(res, f"ser2.loc['{start}':'{end}'] \nNOTE: '2020-01-11' not included!")
# </example>

#
# The problem is that the index is not sorted. The task above requires two
# operations:
#
# <example>
# new_label = '2020-01-11'
# ser2.loc[new_label] = -99
# ser2.sort_index(inplace=True)
#
# start = '2020-01-10'
# end = '2020-01-13'
# res = ser2.loc[start:end]
# printit(res, f"ser2.loc['{start}':'{end}'] \nNOTE: after sorting")
# </example>


# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# Series.iloc: Selection using positions
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------


# ------------------------------------------------------------
# Series.iloc: Selection using a single pos
# ser.iloc[pos] --> scalar if pos <= ser.size
# ------------------------------------------------------------
# printit(ser.size, f"ser.size:")

# Task: Suppose we want to select the first element using iloc
#
#   2020-01-02    7.16 <--
#   2020-01-03    7.19
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The result should be 7.16
pos = 0
res = '?'
# res = ser.iloc[0]

printit(res, f"ser.iloc[{pos}]")

# ------------------------------------------------------------
# Series.iloc: Selection using a seq of positions
# ser.iloc[seq of pos] --> series if pos <= ser.size
# ------------------------------------------------------------
# Task: Suppose we want to select the first and third element
# of the series using iloc and a sequence of positions
#
#   2020-01-02    7.16 <-- Yes
#   2020-01-03    7.19
#   2020-01-06    7.00 <-- Yes
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The result should be a series:
#
#   2020-01-02    7.16
#   2020-01-06    7.00

pos_seq = [0, 2]
res = '?'
# res = ser.iloc[pos_seq]

printit(res, f"ser.iloc[{pos_seq}]")

# ------------------------------------------------------------
# Series.iloc: Selection using slices
#   ser.iloc[slice] --> series
#
# IMPORTANT: Endpoints are NOT included
# ------------------------------------------------------------
# Task: Suppose we want to select the first two elements using iloc
# and slices:
#
#
#   2020-01-02    7.16 <--
#   2020-01-03    7.19 <--
#   2020-01-06    7.00
#   2020-01-07    7.10
#   2020-01-08    6.86
#   2020-01-09    6.95
#   2020-01-10    7.00
#   2020-01-13    7.02
#   2020-01-14    7.11
#   2020-01-15    7.04
#
# The result will be a series:
#
#   2020-01-02    7.16
#   2020-01-03    7.19
#

# Try it first!
start = 0
end = 2
res = '?'
# res = ser.iloc[start:end]

printit(res, f"ser.iloc[{start}:{end}]:")

#
# As before, Pandas will try to return the interval of "positions" included in
# the slice. The slice may be "longer" than the array
#
start = 0
end = 100000
res = '?'
# res = ser.iloc[start:end]

printit(res, f"ser.iloc[{start}:{end}]")

# Very common mistake...
# The problem with the slice below is that it starts at position -1 (the end
# of the array, and then ends at position 0. The slice is "empty" so Pandas
# will return an empty series:
#
start = -1
end = 0
res = '?'
# res = ser.iloc[start:end]

printit(res, f"ser.iloc[{start}:{end}]")

# --------------------------------------------------------------------------------------------
# Series[] : In the past, you could use [] with both positions and labels.
# This was very confusion so this behavior will be deprecated in future
# versions of Pandas.
#
#
# | Selection                     | Result       | Notes                                     |
# |-------------------------------|--------------|-------------------------------------------|
# | Series[label]                 | scalar value | Label must exist, otherwise KeyError      |
# | Series[list of labels]        | Series       | All labels must exist, otherwise KeyError |
# | Series[start_label:end_label] | Series       | Behaviour will vary                       |
# --------------------------------------------------------------------------------------------
# My advice: Always use either loc or iloc, not []

# <example>
# pos = 0
# x1  = ser[pos] # -> Deprecation warning
# res = ser.iloc[pos]
# printit(res, f"This is res")
# printit(x1, f"This is x1")
# </example>

# You can use labels and []
# <example>
# label = '2020-01-02'
# x2  = ser[label]
# res = ser.loc[label]
# printit(res, f"This is res")
# printit(x2, f"This is x2")
# </example>


# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
#   Secting observations from data frames
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------
# df:
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
# 2020-01-06   7.00     3
# 2020-01-07   7.10     4
# 2020-01-08   6.86     5
# 2020-01-09   6.95     6
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10


# ----------------------------------------------------------------------------
# DataFrames.loc[row indexer, col indexer] :  Indexing by row and column labels
#
# where indexer can be:
#
#   - a single label
#   - a sequence of labels
#   - a slice of labels
#
# Note:
#   df.loc[row indexer] same as df.loc[row indexer, :]
#
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# DataFrames.loc using single labels
# ----------------------------------------------------------------------------
#
# Task: Suppose we want to select the following element from DF
#               |
#               V
#             close        bday
# 2020-01-02   7.16 <--     1
# 2020-01-03   7.19         2
# 2020-01-06   7.00         3
# 2020-01-07   7.10         4
# 2020-01-08   6.86         5
# 2020-01-09   6.95         6
# 2020-01-10   7.00         7
# 2020-01-13   7.02         8
# 2020-01-14   7.11         9
# 2020-01-15   7.04        10
#
# The result should be 7.16


# df.loc[row label, col label] --> scalar
rlabel = '2020-01-02'
clabel = 'close'
res = '?'
# res = df.loc[rlabel, clabel]

printit(res, f"df.loc[{rlabel}, {clabel}]")

# Task: Suppose we want to select the following SERIES
#
#   close   7.16
#   bday    1
#
# df.loc[row label] --> df.loc[row label, :]
# In both cases, the result is a SERIES
res1 = '?'
res2 = '?'
# res1 = df.loc[rlabel, :]
# res2 = df.loc[rlabel]

printit(res1, f"This is df.loc['{rlabel}', :]")
printit(res2, f"This is df.loc['{rlabel}']")

# NOTE: The first indexer is for ROWS, not COLS
# df.loc[ column label ] --> KeyError (unless there row with same label exists)

# <example>
# res = df.loc[clabel] # -> KeyError ('close' is not part of df.index)
# </example>

# If you want to select all values for a single column, you must use:
#
# df.loc[:, clabel] --> series with column values (same index)
#
# Tssk: Suppose you want to select the following SERIES from DF:
#
#
# 2020-01-02    7.16
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
#

res = '?'
# res = df.loc[:, 'close']

printit(res, f"df.loc[:, 'close']")

# ----------------------------------------------------------------------------
# DataFrames.loc using seq of labels
#
# NOTE:
#   df.loc[label, seq of labels] --> series with COLUMN labels
#   df.loc[seq of labels, label] --> series with ROW (index) labels
# ----------------------------------------------------------------------------


# -------------------
# df.loc[seq labels, label] --> series with rows as index labels
# df.loc[label, seq labels] --> series with cols as index labels
# -------------------

# Task: We want to select the elements of the column 'close' with row labels
# ['2020-01-02', '2020-01-06']
#
#               |
#               V
#             close        bday
# 2020-01-02   7.16 <--     1
# 2020-01-03   7.19         2
# 2020-01-06   7.00 <--     3
# 2020-01-07   7.10         4
# 2020-01-08   6.86         5
# 2020-01-09   6.95         6
# 2020-01-10   7.00         7
# 2020-01-13   7.02         8
# 2020-01-14   7.11         9
# 2020-01-15   7.04        10
#
# Suppose first, we want the result to be the SERIES
#
# 2020-01-02    7.16
# 2020-01-06    7.00
#
# NOTE: Series only have one index (there is no column index)
#
# This means we need to pass
# - A sequence of row labels
# - A single column label
#
# 1. df.loc[seq labels, label]

rlabel_seq = ['2020-01-02', '2020-01-06']
clabel = 'close'
res = '?'
# res = df.loc[rlabel_seq, clabel]

printit(res, f"df.loc[{rlabel_seq}, '{clabel}'] is:")

# What if we want the result to be a DF?
#
#               close
# 2020-01-02    7.16
# 2020-01-06    7.00
#
# NOTE: DF have two indexes (df.index, df.columns)
#
# This means we need to pass
# - a sequence of row labels
# - a sequence of column labels with ONE VALUE
#
# 2. df.loc[seq labels, [label] ]
rlabel_seq = ['2020-01-02', '2020-01-06']
clabel = 'close'
res = '?'
# res = df.loc[ rlabel_seq, [clabel] ] # Note: [clabel], not clabel

printit(res, f"df.loc[{rlabel_seq}, ['{clabel}'] ] is:")

# So, we will only get a data frame if both row and column indexers are either
# sequences of labels or slices


# Task: We want to select the elements from the DF with row label '2020-01-02'
# and column labels ['close', 'bday']
#
#               |       |
#               V       V
#             close    bday
# 2020-01-02   7.16      1      <--
# 2020-01-03   7.19      2
# 2020-01-06   7.00      3
# 2020-01-07   7.10      4
# 2020-01-08   6.86      5
# 2020-01-09   6.95      6
# 2020-01-10   7.00      7
# 2020-01-13   7.02      8
# 2020-01-14   7.11      9
# 2020-01-15   7.04     10
#
# Suppose first, we want the result to be a DF with one row
#
#             close    bday
# 2020-01-02   7.16      1
#
# We need to pass the following to .loc
# - A sequence with the label '2020-01-02'
# - A sequence with labels ['close', 'bday']

rlabel = '2020-01-02'
rlabel_seq = ['2020-01-02', '2020-01-06']

clabel = 'close'
clabel_seq = ['close', 'bday']

# 3. df.loc[ [label], seq labels]
res = '?'
# res = df.loc[ ['2020-01-02'], ['close', 'bday'] ]

printit(res, f"df.loc[ ['{rlabel}'], {clabel_seq}]")

# Suppose next, we wan the result to be a series with index equal to ['close',
# 'bday]. This series will look like this:
#
#       close    7.16
#       bday     1.00
#
# In this case, we need to pass
# - A single label '2020-01-02'
# - A sequence with labels ['close', 'bday']

# 4. df.loc[ label, seq labels]

res = '?'
# res = df.loc[ '2020-01-02', ['close', 'bday'] ]

printit(res, f"df.loc[ '{rlabel}', {clabel_seq}]")

# ----------------------------------------------------------------------------
# DataFrames.loc using slices
# ----------------------------------------------------------------------------

# Suppose we want to select the following elements from DF using slices
#
#
#                bday  close
#   2020-01-10      7   7.00
#   2020-01-13      8   7.02
#   2020-01-14      9   7.11
#   2020-01-15     10   7.04
#
#
# Note that the order of the columns is different from the original DF

# We could try to pass the following slices:
#
# '2020-01-10':'2020-01-15'
# 'bday':'close'
#
# But this will not work:
res = '?'
# res = df.loc[\
#      '2020-01-10':'2020-01-15',
#      'bday':'close']

printit(res, f"df.loc['2020-01-10':'2020-01-15','bday':'close']")

# The result is an empty DF. This is because the order of the columns in
# the original DF is ['close', 'bday']. There is no interval of column labels
# that is included in a slice that starts with 'bday' and ends with 'close'.
#
# However, the following will work:
#
# <example>
# res = df.loc[
#      '2020-01-10':'2020-01-15',
#      'bday':'close':-1,
#       ]
# printit(res, f"df.loc['2020-01-10':'2020-01-15','bday':'close']")
# </example>

# This is because the slice 'bday':'close':-1, will find the interval from
# 'bday' to 'close' but in REVERSE:


# In fact, the following can be used to reverse the columns of any data frame
# <example>
# res = df.loc[:, ::-1]
# printit(res, f"df.loc[:, ::-1]")
# </example>


# DELETE
# The other alternative is to sort the column index first:
# <example>
# df2 = df.copy()
# df2.sort_index(axis=1, inplace=True)
# res = df2.loc[ \
#      '2020-01-10':'2020-01-15',
#      'bday':'close']
# printit(res, f"df2.loc['2020-01-10':'2020-01-15','bday':'close']")
# </example>


# ----------------------------------------------------------------------------
# Exercise: Use df.loc[slice, label] so the following series is returned
#   2020-01-10     7
#   2020-01-13     8
#   2020-01-14     9
#   2020-01-15    10
# ----------------------------------------------------------------------------
res = '?'
# res = df.loc['2020-01-10':'2020-01-15', 'bday']

printit(res)

# ----------------------------------------------------------------------------
# Exercise: Use df.loc['2020-01-02', slide] WITHOUT MODIFYING DF,
# so the following series is returned for '2020-01-02':
#  close    7.16
#  bday     1.00
# ----------------------------------------------------------------------------
rlabel = '2020-01-02'
res = '?'
# Remember that 'label':  will return all obs from 'label' until the end
# of the index
# res = df.loc[rlabel, 'close':]

printit(res)

# ----------------------------------------------------------------------------
# DataFrames.iloc[row indexer, col indexer] :  Indexing by row and column positions
#
# where indexer can be:
#
#   - a single position
#   - a sequence of positions
#   - a slice of positions
#
# Note:
#   df.iloc[row indexer] same as df.iloc[row indexer, :]
#
# ----------------------------------------------------------------------------

# Analogous to moving from ser.loc to ser.iloc. Will be left as an exercise

# ----------------------------------------------------------------------------
# DataFrames.iloc using single labels
# ----------------------------------------------------------------------------

# Exercise: Use df.iloc to return the following ELEMENT from the DF
#
#                 |
#                 v
#               close       bday
#   2020-01-02   7.16         1
#   2020-01-03   7.19 <--     2
#   2020-01-06   7.00         3
#   2020-01-07   7.10         4
#   2020-01-08   6.86         5
#   2020-01-09   6.95         6
#   2020-01-10   7.00         7
#   2020-01-13   7.02         8
#   2020-01-14   7.11         9
#   2020-01-15   7.04        10
#
# The result should be 7.19
res = '?'
# res = df.iloc[1, 0]

printit(res)

# Exercise: Use df.iloc[pos] to select the last row of df, which will be the
# following SERIES:
#
#   close     7.04
#   bday     10.00
#
res = '?'
# res = df.iloc[-1]   # Or df.iloc[-1, :]

printit(res)

# ----------------------------------------------------------------------------
# DataFrames.iloc using seq of labels and slices
# ----------------------------------------------------------------------------
# Exercise: Use .iloc to produce the following objects from the df
#
# NOTE: There are multiple ways to complete the same task. As long as the
# object returned is correct, you are free to choose the approach that best
# suits you

# 1. A DF with all rows from df but with the columns in reverse order:
#
#               bday  close
#   2020-01-02     1   7.16
#   2020-01-03     2   7.19
#   2020-01-06     3   7.00
#   2020-01-07     4   7.10
#   2020-01-08     5   6.86
#   2020-01-09     6   6.95
#   2020-01-10     7   7.00
#   2020-01-13     8   7.02
#   2020-01-14     9   7.11
#   2020-01-15    10   7.04
#
res1 = '?'
# res1 = df.iloc[:, ::-1]

printit(res1)

# res1  = df.iloc[:, [1, 0]]
# printit(res1)



# 2. A SERIES with the last two values from the 'bday' column:
#
#   2020-01-14    7.11
#   2020-01-15    7.04
res2 = '?'
# res2 = df.iloc[-2:, 0]

printit(res2)

# 3. a DF with the first two rows of df (and all columns)
#
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
#
res3 = '?'
# res3 = df.iloc[:2]

printit(res3)

# ----------------------------------------------------------------------------
# DataFrames.iloc using slices
# ----------------------------------------------------------------------------
# Exercise:
# Use .iloc and slices to produce the following objects from the df
#
# NOTE: There are multiple ways to complete the same task. As long as the
# object returned is correct, you are free to choose the approach that best
# suits you

# 1. A DF with all rows from df except the first one:
#
#               close  bday
#   2020-01-03   7.19     2
#   2020-01-06   7.00     3
#   2020-01-07   7.10     4
#   2020-01-08   6.86     5
#   2020-01-09   6.95     6
#   2020-01-10   7.00     7
#   2020-01-13   7.02     8
#   2020-01-14   7.11     9
#   2020-01-15   7.04    10
res1 = '?'
# res1 = df.iloc[1:]

printit(res1)

# 2. a DF (NOT A SERIES) with the last column of df:
#
#               bday
#   2020-01-02     1
#   2020-01-03     2
#   2020-01-06     3
#   2020-01-07     4
#   2020-01-08     5
#   2020-01-09     6
#   2020-01-10     7
#   2020-01-13     8
#   2020-01-14     9
#   2020-01-15    10
#

res2 = '?'
# res2 = df.iloc[:, -1:]

printit(res2)

# 3. A DF with the first two rows of df (using slices, not seq of positions):
#
#             close  bday
# 2020-01-02   7.16     1
# 2020-01-03   7.19     2
#
res3 = '?'
# res3 = df.iloc[:2]

printit(res3)

# 4. A df with the last 100 (one hundred) rows from df (assume you don't know how many
#   rows the data frame df has)
res4 = '?'
# The result will the entire DF
# res4 = df.iloc[-100:]

printit(res4)

# ----------------------------------------------------------------------------
# DataFrames and []
#
# | Selection            | Result | Notes                              |
# |----------------------|--------|------------------------------------|
# | df[colname]          | series | colname must exist                 |
# | df[list of colnames] | df     | All colname must exist             |
# | df[slices]           | df     | Operates on row index, not columns |
# ----------------------------------------------------------------------------

# df[label] --> series with the elements from the COLUMN labeled 'label'
#
# Exercise: Select the SERIES with the elements from the column 'close':
#
#
# 2020-01-02    7.16
# 2020-01-03    7.19
# 2020-01-06    7.00
# 2020-01-07    7.10
# 2020-01-08    6.86
# 2020-01-09    6.95
# 2020-01-10    7.00
# 2020-01-13    7.02
# 2020-01-14    7.11
# 2020-01-15    7.04
res = '?'
# res  = df['close']

printit(res)

# df[seq of labels] --> DF with the column labels in the order provided
#
# Exercise: The data frame with the columns in reversed order (using seq of
# values, not slides)
#
#             bday  close
# 2020-01-02     1   7.16
# 2020-01-03     2   7.19
# 2020-01-06     3   7.00
# 2020-01-07     4   7.10
# 2020-01-08     5   6.86
# 2020-01-09     6   6.95
# 2020-01-10     7   7.00
# 2020-01-13     8   7.02
# 2020-01-14     9   7.11
# 2020-01-15    10   7.04
#
clabel_seq = ['bday', 'close']
res = '?'
# res = df[clabel_seq]

printit(res)

# df[slice of ROW labels] --> DF with those ROWS
#
# NOTE: df[slice] OPERATE OVER ROWS, NOT COLUMNS
#
# Exercise: Use df[slice] to select all observations from 2020-02-10
# to 2020-01-15:
#
#             close  bday
# 2020-01-10   7.00     7
# 2020-01-13   7.02     8
# 2020-01-14   7.11     9
# 2020-01-15   7.04    10
#
rstart = '2020-01-10'
rend = '2020-01-15'
res = '?'
# res = df[rstart:rend]

printit(res)

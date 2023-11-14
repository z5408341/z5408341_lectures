""" week7_slides_p2.py

Scaffold and solutions to the codes we discussed during the second part of the
class (Week 7)



"""

import os
import pprint as pp

import pandas as pd

import toolkit_config as cfg

# Variables with the location of the following files
# toolkit/
# |__ data/
# |   |__ qan_prc_2020.csv           <- Exists
# |   |__ qan_prc_no_header.csv      <- Will be created
# |   |__ qan_prc_no_index.csv       <- Will be created

QAN_PRC_CSV = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
QAN_NOHEAD_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_header.csv')
QAN_NOINDEX_CSV = os.path.join(cfg.DATADIR, 'qan_prc_no_index.csv')


def print_df(df):
    """ Prints the contents of `df` along with some information
    Parameters
    ----------
    df : data frame

    """
    if isinstance(df, str) and df == '?':
        return
    elif not isinstance(df, pd.DataFrame):
        raise Exception("Parameter `df` must be a data frame")
    sep = '-' * 40
    to_print = [
        '',
        sep,
        pp.pformat(df),
        '',
    ]
    print('\n'.join(to_print))
    df.info()
    print('\n'.join(['', sep]))


# ----------------------------------------------------------------------------
#   Reading data from a CSV file
# ----------------------------------------------------------------------------

# Alternative 1:
#
# Load the data contained in qan_prc_2020.csv to a DF
# and then set the index using the .set_index method
qan_naive_read = '?'
# qan_naive_read  = pd.read_csv(QAN_PRC_CSV)
# qan_naive_read.set_index('Date', inplace=True)

print_df(qan_naive_read)

# Alternative 2: use the index_col parameter
qan_better_read = '?'
# qan_better_read  = pd.read_csv(QAN_PRC_CSV, index_col='Date')

print_df(qan_better_read)

# ----------------------------------------------------------------------------
#   Storing data to a CSV file
# ----------------------------------------------------------------------------
# First, we read the data into a dataframe (without setting the index)
# Then save it using he .to_csv method
# qan_prc = pd.read_csv(QAN_PRC_CSV)

# We then save the data into the file located at QAN_NOHEAD_CSV above.
# If we set the parameter header to False, the header columns will not be saved
# qan_prc.to_csv(QAN_NOHEAD_CSV, header=False)


# If we want the column headers but not the index, we can set the parameter 'index'
# to False
# qan_prc.to_csv(QAN_NOINDEX_CSV, index=False)


# ----------------------------------------------------------------------------
#  read_csv and to_csv have many useful parameters, which we will discuss later
# in the course
# ----------------------------------------------------------------------------

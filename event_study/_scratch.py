""" _scratch.py

Scratch pad...
"""

import os

import pandas as pd
import yfinance as yf

import toolkit_config as tk_cfg


# ---------------------------------------------------
# Constants
# ---------------------------------------------------
TIC = 'tsla'
PRC_CSV = os.path.join(tk_cfg.DATADIR , 'tsla_prc.csv')
START = '1900-01-01'
END = '2020-12-31'


# ---------------------------------------------------
# get_data0
# ---------------------------------------------------
def get_data0(tic):
    """ Draft of the get_data function. Will download and save stock prices.

    Parameters
    ----------
    tic : str
        Ticker

    """
    df = yf.download(tic,
                     start=START,
                     end=END,
                     )
    df.to_csv(PRC_CSV)


# ---------------------------------------------------
# get_data1
# ---------------------------------------------------
def get_data1(tic):
    """ Draft of the get_data function. Will download and save stock prices.

    Parameters
    ----------
    tic : str
        Ticker

    """
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR , filename)
    df = yf.download(tic,
                     start=START,
                     end=END,
                     )
    df.to_csv(pth)


def load_prc0(tic):
    """ Loads the stock prices saved by get_data

    Parameters
    ----------
    tic : str
        Ticker

    """
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR , filename)
    df = pd.read_csv(pth)
    print(df)


def load_prc1(tic):
    """ Loads the stock prices saved by get_data

    Parameters
    ----------
    tic : str
        Ticker

    """
    filename = f'{tic}_prc.csv'
    pth = os.path.join(tk_cfg.DATADIR , filename)
    df = pd.read_csv(pth)

    d = {c:c.lower() for c in df.columns}
    # d = {
    #   'Date': 'date',
    #   'Open': 'open',
    #   'High': 'high',
    #   'Low': 'low',
    #   'Close': 'close',
    #   'Adj Close': 'adj close',
    #   'Volume': 'volume',
    #   }
    df = df.rename(columns=d)
    df.info()

if __name__ == "__main__":
    #get_data0(tic=TIC)
    #get_data1(tic=TIC)
    #load_prc0(tic=TIC)
    #load_prc1(tic=TIC)
    pass


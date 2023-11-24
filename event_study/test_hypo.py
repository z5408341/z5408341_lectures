""" test_hypo.py

Utilities to test the hypothesis in the study
"""

import pandas as pd

def calc_tstats(event_cars):
    """ Compute a t-stat for each event type in the dataframe `event_df`.

    Parameters
    ----------
    event_cars : dataframe
        Dataframe with event types and CARs for each event in the sample.

    """
    groups = event_cars.groupby('event_type')['car']
    print(groups.describe())
    car_bar = groups.mean()
    car_sem = groups.sem()
    car_t = car_bar/car_sem
    car_n = groups.count()
    res = pd.DataFrame({'car_bar':car_bar, 'car_t': car_t, 'n_obs': car_n})
    return res



import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.dates import date2num, num2date
from matplotlib import dates as mdates
from matplotlib import ticker
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

from scipy import stats as sps
from scipy.interpolate import interp1d

from IPython.display import clear_output



file = "dataset1.csv"
states = pd.read_csv(file,
                     usecols=['TimeStampDate', 'CountyName', 'ConfirmedCovidCases'],
                     parse_dates=['TimeStampDate'],
                     index_col=['CountyName', 'TimeStampDate'],
                     squeeze=True).sort_index()


state_name = 'Dublin'

def prepare_cases(cases):
    new_cases = cases.diff()

    smoothed = new_cases.rolling(9,
        win_type='gaussian',
        min_periods=1,
        center=True).mean(std=3).round()

    idx_start = np.searchsorted(smoothed, 10)

    smoothed = smoothed.iloc[idx_start:]
    original = new_cases.loc[smoothed.index]

    return original, smoothed

cases = states.xs(state_name).rename(f"{state_name} cases")

original, smoothed = prepare_cases(cases)

original.plot(title=f"{state_name} New Cases per Day",
               c='k',
               linestyle=':',
               alpha=.5,
               label='Actual',
               legend=True,
             figsize=(500/72, 400/72))

ax = smoothed.plot(label='Best Fit',
                   legend=True)

ax.get_figure().set_facecolor('w')
plt.show()

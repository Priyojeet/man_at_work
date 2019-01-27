import numpy as np
import pandas as pd


dti = pd.date_range(start='2015-01-01', end='2015-12-31', freq='B')
s = pd.Series(np.random.rand(len(dti)), index=dti)
print(s)

print(s[dti.weekday ==2].sum())
print(s.resample('M').mean())
print(s[dti.month].mean())
print(s.groupby(pd.TimeGrouper('4M')).idxmax())

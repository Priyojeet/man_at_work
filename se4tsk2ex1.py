import pandas as pd
df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
#print(df)
x = (df['X'] != 0).cumsum()
y = (x != x.shift())
df['Y'] = y.groupby((y != y.shift()).cumsum()).cumsum()
print(df)
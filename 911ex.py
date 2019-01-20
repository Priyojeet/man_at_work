import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("911.csv")
df.info()
print(df.head())
print(df['zip'].head())
print(df['twp'].head())
print(df['title'].nunique())
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
print(df['Reason'].head())
print(df['Reason'].value_counts())
print(type(df['timeStamp'][0]))
df['timeStamp'] = pd.to_datetime(df['timeStamp'])
print(type(df['timeStamp'][0]))
print(df['timeStamp'][5])
print(df['timeStamp'][5].hour)
print(df['timeStamp'][5].month)
df['Month'] = df['timeStamp'].apply(lambda timestamp: timestamp.month)
df['Hour'] = df['timeStamp'].apply(lambda timestamp: timestamp.hour)
df['Day_of_week'] = df['timeStamp'].apply(lambda timestamp: timestamp.weekday())
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day_of_week'] = df['timeStamp'].apply(lambda timestamp: timestamp.weekday()).map(dmap)
print(dmap)
print(df['Day_of_week'])
dayMonth = df.groupby(by=['Day_of_week','Month']).count()['Reason'].unstack()
print(dayMonth)
sns.countplot(x='Reason',data=df,palette='viridis')
plt.show()
sns.countplot(x='Day_of_week',data=df,hue='Reason',palette='viridis')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
sns.countplot(x='Month',data=df,hue='Reason',palette='viridis')
plt.show()
byMonth = df.groupby('Month').count()
byMonth.head()
byMonth['twp'].plot()
plt.show()
sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())
plt.show()

df['Date']=df['timeStamp'].apply(lambda t: t.date())
df.groupby('Date').count()['twp'].plot()
plt.tight_layout()
plt.show()

df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.title('Traffic')
plt.tight_layout()
plt.show()

df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.title('Fire')
plt.tight_layout()
plt.show()

df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.title('EMS')
plt.tight_layout()
plt.show()

dayHour = df.groupby(by=['Day_of_week','Hour']).count()['Reason'].unstack()
dayHour.head()
plt.figure(figsize=(12,6))
sns.heatmap(dayHour,cmap='viridis')
plt.show()

sns.clustermap(dayHour,cmap='viridis')
plt.show()

plt.figure(figsize=(12,6))
sns.heatmap(dayMonth,cmap='viridis')
plt.show()

sns.clustermap(dayMonth,cmap='viridis')
plt.show()
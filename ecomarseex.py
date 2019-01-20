import pandas as pd

data = pd.read_csv("Ecommerce Purchases")
print(data.head())
data.info()
print(data["Purchase Price"].mean())
print(data["Purchase Price"].min())
print(data["Purchase Price"].max())
print(data[data["Language"]=='en'].count())
data[data["Job"]=='Lawyer'].info()
print(data['AM or PM'].value_counts())
print(data['Job'].value_counts().head(5))
print(data[data['Lot']=='90WT']['Purchase Price'])
print(data[data['Credit Card']==4926535242672853]['Email'])
print(data[(data['CC Provider'] == 'American Express') & (data['Purchase Price']>95)].count)


def year_expire(date):
    return data.split('/')[1]


print(data[data['CC Exp Date'].apply(year_expire) == '25']['CC Exp Date'].count())


def email_pro(email):
    return email.split('@')[1]


print(data['Email'].apply(email_pro).value_counts().head(5))

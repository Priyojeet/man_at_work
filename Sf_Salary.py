import pandas as pd

sal = pd.read_csv('Salaries.csv')
print(sal.head())
print(sal.info())
print(sal['BasePay'].mean())
print(sal['OvertimePay'].max())
print(sal[sal['EmployeeName']=="JOSEPH DRISCOLL"]['JobTitle'])
print(sal[sal['EmployeeName']=="JOSEPH DRISCOLL"]['TotalPayBenefits'])
print(sal[sal['TotalPayBenefits'] == max(sal['TotalPayBenefits'])])
print(sal[sal['TotalPayBenefits'] == min(sal['TotalPayBenefits'])])
print(sal.groupby('Year').mean()['BasePay'])
print(sal['JobTitle'].nunique())
print(sal.groupby('JobTitle').count().sort_values(by='Id', ascending=False)['Id'].head(5))


job_counts_2013 = sal[sal['Year'] == 2013]['JobTitle'].value_counts()
print(job_counts_2013[job_counts_2013 == 1].sum())


def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False


print(sal['JobTitle'].apply(chief_string).sum())

sal['TitleLen'] = sal['JobTitle'].apply(len)
print(sal[['TitleLen', 'TotalPayBenefits']].corr())

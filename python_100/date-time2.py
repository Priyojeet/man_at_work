# Python program to determine whether a given year is a leap year.

import datetime
def leap_year(y):
    if y % 400 == 0:
        return True
    if y % 100 == 0:
        return False
    if y % 4 == 0:
        return True
    else:
        return False
print(leap_year(1900))

# Python program to convert unix timestamp string to readable date.
print(
    datetime.datetime.fromtimestamp(
        int("1284105682")
    ).strftime('%Y-%m-%d %H:%M:%S')
)

# Python program to print yesterday, today, tomorrow.

today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print('Yesterday : ',yesterday)
print('Today : ',today)
print('Tomorrow : ',tomorrow)

import sys

a = int(input("enter the 1st value:-"))
b = int(input("enter the 2nd value:-"))
try:
    c = a/b
except:
    error = sys.exc_info()[0]
    print(error)
else:
    print("all fine.")
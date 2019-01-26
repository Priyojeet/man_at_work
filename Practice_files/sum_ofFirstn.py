import sys
def sum(arg):
    sum_num = (arg*(arg+1))/2
    return sum_num
try:
    n = int(input("enter the number you want:-"))
except:
    error= sys.exc_info()[0]
    print(error)
else:
    print(sum(n))

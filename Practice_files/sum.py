import sys
try:
    number = int(input("enter the number you want:-"))
except:
    error = sys.exc_info()[0]
    print(error)
else:
    def sum_number(arg):
        count = 0
        for i in range(arg):
            count += i
        print(count)
    sum_number(number)

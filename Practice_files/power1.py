import sys
try:
    number = int(input("enter the number you want:-"))
    power_number = int(input("enter the power you want:-"))
except:
    error = sys.exc_info()[0]
    print(error)
else:
    def powr(num, n):
        if(n<=0):
            print("result is 0")
        else:
            result = 1
            for i in range(1,n+1):
                result *= num
            print(result)
    powr(number, power_number)

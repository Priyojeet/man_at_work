import sys
try:
    number = int(input("enter the number:-"))
    power = int(input("enter the power number:-"))
except:
    error=sys.exc_info()[0]
    print(error)
else:
    def powr(n,p):
        if(p==0):
            return 1
        answer=n
        increment=n
        for i in range(1,p):
            for j in range(1,n):
                answer+=increment
            increment=answer
        return answer
    print(powr(number, power))

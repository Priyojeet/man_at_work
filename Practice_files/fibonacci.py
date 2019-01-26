def fib(n):
    a = int(input("enter the 1st number:-"))
    b = int(input("enter the 2nd number:-"))
    print(a,b,end=" ")
    while(n-2):
        c = a+b
        a = b
        b = c
        print(c, end=" ")
        n = n-1
fib(6)

def fib_rec(n):
    if(n<=1):
        return n
    else:
        return(fib_rec(n-1) + fib_rec(n-2))

terms = 10
if terms<=0:
    print("please enter a valid integer:-")
else:
    print("fibonacci sequence is:-")
    for i in range(terms):
        print(fib_rec(i))

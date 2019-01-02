def myfilter(func, arg):
    l = []
    for i in arg:
        if func(i):
            l.append(i)
    return l
def isprime(arg):
    prime = True
    if(arg>1):
        for i in range(2, arg):
            if(arg%i == 0):
                prime = False
            if(prime==True):
                return True
            else:
                return False

list = []
length = int(input("enter the length of your list:-"))
for item in range(length):
    i = int(input("enter the element of your list:-"))
    list.append(i)
print(list)
print(myfilter(isprime, list))


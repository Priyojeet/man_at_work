def gcd(x, y):
    gcd =1
    if x%y == 0:
        return y
    for k in range(int(y/2),0,-1):
        if x%k == 0 and y%k ==0:
            gcd = k
            break
    return gcd


a=int(input("enter the number:-"))
b=int(input("enter 2nd number:-"))
print(gcd(a,b))



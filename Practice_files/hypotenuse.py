from math import sqrt


def hypotenuse(arg1, arg2):
    c = sqrt(arg1**2 + arg2**2)
    return c


a = float(input("enter the a value:-"))
b = float(input("enter the b value:-"))
print(hypotenuse(a, b))

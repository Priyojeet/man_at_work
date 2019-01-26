def add_numbers(a,b):
    if not(isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    return a+b
#print(add_numbers("t",8))

def take_input():
    x=eval(input("enter the x value:-"))
    y=eval(input("enter the y value:-"))
    print(add_numbers(x,y))
take_input()
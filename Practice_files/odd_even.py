number = eval(input("enter the number you want:-"))
def odd_even_check(arg):
    if(isinstance(arg, str)):
        print("please enter a valid integer.")
    else:
        if(arg%2==0):
            print("entered number is even")
        else:
            print("entered number is odd")
odd_even_check(number)

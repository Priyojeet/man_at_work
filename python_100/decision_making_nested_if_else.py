# check prime number with nested loop

number = eval(input("enter the number you want:-"))
if(isinstance(number,str)):
    print(" please enter an integer value")
elif(type(number) == float):
    print("you enter a float number")
else:
    if (number <= 0):
        print("enter an integer grater then 0")
    elif (number == 1):
        print("you have enter 1")
    else:
        for i in range(2, number):
            if ((number % i) == 0):
                print("number is not prime")
                break
        else:
            print("number is prime")
number = int(input("enter the number you want:-"))
for i in range(number):
    for j in range(i):
        print("* ", end="")
    print(" ")
for i in range(number, 0, -1):
    for j in range(i):
        print("* ", end="")
    print(" ")

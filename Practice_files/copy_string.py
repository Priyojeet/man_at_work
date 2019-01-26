number = int(input("enter the how many copy you want:-"))
name = str(input("enter the name you want to copy:-"))
def cpy(arg, n):
    result = ""
    for i in range(n):
        result = result+" "+arg
    return result
print(cpy(name, number))

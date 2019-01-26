def substring_copy(arg, n):
    flen = int(input("enter the index:-"))
    if flen == len(arg):
        flen = len(arg)
    substr = arg[:flen]
    result = ""
    for i in range(n):
        result = result+substr
    return result


string = str(input("enter the string:-"))
index = int(input("enter how many copy you want:-"))
print(substring_copy(string,index))

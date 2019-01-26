import sys
try:
    length = int(input("enter the number of colour you want:-"))
except:
    error = sys.exc_info()[0]
    print(error)
else:
    colour_list = []
    for elements in range(length):
        try:
            colour = str(input("enter the colours you want:-"))
        except:
            error1 = sys.exc_info()[0]
            print(error1)
        else:
            colour_list.append(colour)
    print(list)
    print("%s%s"%(colour_list[0],colour_list[-1]))

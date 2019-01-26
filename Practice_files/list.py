import sys
l = []
try:
    length = int(input("enter the length of the list:-"))
except:
    error = sys.exc_info()[0]
    print(error)
else:
    def make_list(arg):
        for i in range(arg):
            element = eval(input("enter the elements you want in list:-"))
            if(isinstance(element,str)):
                print("please enter an integer.")
                exit()
            else:
                l.append(element)
        print(l)
    make_list(length)

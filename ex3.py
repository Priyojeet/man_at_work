fname = str(input("enter first name:-"))
lname = str(input("enter last name:-"))
name = fname+" "+lname
#print(name)
def rev(arg):
    s = ""
    for i in arg:
        s=i+s
    print(s)
rev(name)

l = int(input("enter the length of your list:-"))
lst =[]
for i in range(l):
    element = int(input("enter the elements you want:-"))
    lst.append(element)
def count_length(arg):
    count=0
    for j in arg:
        count+=1
    print(count)

'''def while_count(arg):
    count = 0
    while(arg[count] != None):
        count+=1
    print(count)'''


count_length(lst)
#while_count(lst)

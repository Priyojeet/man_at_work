def chrcnt(arg):
    count = 0
    for i in arg:
        count = count+1
    return count
def find_longest(arg):
        max = chrcnt(arg[0])
        for i in arg:
            if(chrcnt(i)>max):
                max = chrcnt(i)
        for j in arg:
            if(chrcnt(j)==max):
                return j
l = []
length = int(input("enter the number of words you want:-"))
for i in range(length):
    item = str(input("enter a word:-"))
    l.append(item)
print(find_longest(l))

l = [1,5,2,4,3,2,6,3,4]
def count_duplicate(arg):
    count = 0
    for i in range(len(arg)):
        for j in range(i+1,len(arg)):
            if(arg[i] == arg[j]):
                count+=1
                break
    return count
print(count_duplicate(l))

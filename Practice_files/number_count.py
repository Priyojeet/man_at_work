length = int(input("enter the number of elements you want:-"))
def count_duplicate(arg):
    count = 0
    for i in range(len(arg)):
        for j in range(i + 1, len(arg)):
            if (arg[i] == arg[j]):
                count += 1
                break
    return count


def create_list(arg):
    l=[]
    for i in range(arg):
        elements = int(input("enter the elements :-"))
        l.append(elements)
    print(count_duplicate(l))
create_list(length)

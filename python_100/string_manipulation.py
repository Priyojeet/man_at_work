# Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest(arg):
    l = []
    for i in arg:
        count = 0
        for j in i:
            count += 1
        l.append(count)
    l.sort()
    return l[-1]


length = int(input("enter the number of length :-"))
n_l = []
for i in range(length):
    element = str(input("enter a string:-"))
    n_l.append(element)

print(find_longest(n_l))


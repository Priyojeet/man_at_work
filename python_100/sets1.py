# remove any element if present in set

num_set = set([0, 1, 3, 4, 5])

def remove(arg, number):
    my_set = arg.copy()
    for i in arg:
        if i == number:
            my_set.remove(i)
    print(my_set)

remove(num_set, 4)
# Python program for binary search for an ordered list.

def bsearch(list, item):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == item:
            return True
        else:
            if item < list[midpoint]:
                return search(list[:midpoint], item)
            else:
                return search(list[midpoint + 1:], item)


def search(nlist, item):
    first = 0
    last = len(nlist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if nlist[midpoint] == item:
            found = True
        else:
            if item < nlist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


print(bsearch([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
print(bsearch([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

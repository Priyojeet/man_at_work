def duplicate(x):
    size = len(x)
    repeted = []
    for i in range(size):
        k=i+1
        for j in range(k, size):
            if x[i] == x[j] and x[i] not in repeted:
                repeted.append(x[i])
    return repeted

def remove(x):
    final_l=[]
    for num in x:
        if num not in final_l:
            final_l.append(num)
    return final_l

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict


list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(duplicate(list1))
print(remove(list1))
y=char_frequency(list1)

def get_key(dictofEle, value):
    listofkeys = list()
    listofitems = dictofEle.items()
    for item in listofitems:
        if item[1] == value:
            listofkeys.append(item[0])
    return listofkeys

print(get_key(y, 3))

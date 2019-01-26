def concate_listData(arg):
    result = ""
    for i in arg:
        result = result+str(i)
    return result
print(concate_listData([2,5,4,6,12]))

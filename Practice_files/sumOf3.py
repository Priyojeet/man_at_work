def sum(x, y, z):
    if x==y or y==z or x==z:
        sum = 0
    else:
        sum = x+y+z
    return sum
print(sum(2,1,3))
print(sum(2,1,2))

def test_number(x,y):
    if x==y or abs(x-y)==5 or (x+y)==5:
        return True
    else:
        return False
print(test_number(3,2))
print(test_number(7,2))
print(test_number(9,1))
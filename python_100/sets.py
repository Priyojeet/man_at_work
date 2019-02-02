# some set operations

c_set = set()  # empty set
c_set.add(3)  # add single item
print(c_set)
c_set.update([4,5,6,7])  # add multiple
print(c_set)
c_set.pop()  # removing elements
print(c_set)
c_set.remove(5)  # removing element
print(c_set)
c_set.difference_update({5,6})  # removing multiple elements
print(c_set)
c_set.update([1,2,3,5,6])
print(c_set)
c_set1 = set([1, 3, 5, 6, 3, 7,8,9])
print(c_set1)

c_set2 = c_set1 & c_set
print(c_set2)
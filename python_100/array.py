# Write a Python program to convert an array to an ordinary list with the same items.

import array


array_num = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
for i in range(len(array_num)):
    print(array_num[i], end=" ")
print("\nOriginal array: "+str(array_num))
num_list = array_num.tolist()
print(num_list)

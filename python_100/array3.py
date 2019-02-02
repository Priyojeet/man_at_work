# Write a Python program to append items from a specified list.

import array


num_list = [1, 2, 6, -8]
array_num = array.array('i', [])
print("Items in the list: " + str(num_list))
print("Append items from the list: ")
array_num.fromlist(num_list)
print("Items in the array: "+str(array_num))

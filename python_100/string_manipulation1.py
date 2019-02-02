# Write a Python program to remove the nth index character from a nonempty string.


def remove_char(str, n):
    slice1 = str[:n]
    slice2 = str[n + 1:]
    #print(slice1)
    #print(slice2)
    return slice1 + slice2


l = str(input("enter a string:-"))
no = int(input("enter a number:-"))


print(remove_char(l, no))

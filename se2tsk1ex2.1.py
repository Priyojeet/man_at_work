l = []
s = str(input("enter the string:-"))
for i in s:
    l.append(i)
print(l)

# comprehension
char_l = [char for char in s]
print(char_l)
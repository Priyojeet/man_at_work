x = 1
y = 1.0
print(type(x))
print(type(y))
b1 = True
b2 = False
print(type(b1), type(b2))
name = "jeet"
print(type(name))
x = 1.0 - 2.0j
print(x)
print(x)
print(x.real, x.imag)
# print('day'+ 1) error
print('day'+ str(1))

# condition statements

i = 3
if i<3:
    # operation you want to perform if condition satisfied.
    print("less then 3")
elif i<5:
    # operation you want to perform else if this condition satisfied.
    print('less then 5')
else:
    # operation you want to perform if condition got failed.
    print('5 or more.')
# playing with list
l = []  # empty list declaration
a_l = list()  # another way of list declaration
print(l,a_l)
l = [1,2,3,4]  # python will update the value of list l.
print(l)
l2 = list(l)
print(l2)
print(list('abcdef'))  # python will convert it into a list of alphabet.
l.append(6)  # adding elements in the list.
print(l)
l.insert(4, 5)  # updating the value on 4th index.
print(l)


#  loop control statements
# for loop
sum = 0
for items in l:
    sum = sum+items
print(sum)

for items in l:
    print(items)
else:
    print("no items left!")

# while loop
n = len(l)
sum = 0
i = 0
while i< n:
    sum = sum+l[i]
    i += 1
print(sum)

for items in l:
    if items == 5:
        continue
    print(items)
print("end")

for items in l:
    if items == 4:
        break
    print(items)
print("end of the operation")

s = "hello world"
print(s[::-1])
s = s+" add me"
print(s)
print(s.title())
print(s.split('o'))
print(s.find('r'))
print(s.center(50,"-"))

popped_Item = l.pop()
print(popped_Item)
print(l)


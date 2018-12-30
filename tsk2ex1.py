sequence = str(input("enter the comma separated numbers:-"))
list = sequence.split(",")
l = []
for i in list:
    l.append(int(i))
print(l)

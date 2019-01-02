l = []
txt = str(input("enter the text:-"))
for i in txt:
    for j in range(1, 5):
        item = i * j
        l.append(item)
print(l)
# comprehension

list = [i*j for i in txt for j in range(1,5)]
print(list)

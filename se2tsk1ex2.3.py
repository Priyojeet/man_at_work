l = []
txt = str(input("enter the text:-"))
for i in range(1,5):
    for j in txt:
        item = i*j
        l.append(item)
print(l)
# comprehension

n_list = [i*j for i in range(1,5) for j in txt]
print(n_list)

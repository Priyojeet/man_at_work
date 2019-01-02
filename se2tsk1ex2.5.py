l = []
n_l = [int(input("enter the item:-")) for i in range(4)]
print(n_l)
for i in range(0,4):
    l.append([])
    for j in n_l:
        item = j+i
        l[i].append(item)
print(l)

# comprehension

c_list = [[i+j for i in n_l] for j in range(0,4)]
print(c_list)

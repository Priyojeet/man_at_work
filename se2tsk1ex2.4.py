l = []
n_l = [int(input("enter the item:-")) for i in range(3)]
print(n_l)

for i in n_l:
    for j in range(0,3):
        item = [i+j]
        l.append(item)
print(l)

# comprehension

c_list = [[i+j] for i in n_l for j in range(0,3)]
print(c_list)

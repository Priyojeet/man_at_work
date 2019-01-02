l = []
n_l = []
for i in range(3):
    item = int(input("enter the item:-"))
    l.append(item)
for a in l:
    for b in l:
        n_item = (b, a)
        n_l.append(n_item)
print(n_l)

# comprehension

n_l = [(b,a) for a in l for b in l]
print(n_l)
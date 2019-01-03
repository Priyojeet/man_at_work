length = int(input("enter how many words you want in your list:-"))
l = []
new_l = []
for i in range(length):
    word = str(input("enter the word:-"))
    l.append(word)


def num_rep(arg):
    for item in arg:
        count = 0
        for ch in item:
            count = count+1
        new_l.append(count)
    print(new_l)


num_rep(l)

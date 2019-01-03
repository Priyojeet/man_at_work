number = int(input("enter the number:-"))
length = int(input("enter how many words you want in your list:-"))
l = []
for i in range(length):
    word = str(input("enter the word:-"))
    l.append(word)


def word_length(arg):
    count = 0
    for char in arg:
        count = count+1
    return count


def filter_long_words(arg, no):
    new_l = []
    for word in arg:
        if(word_length(word) >= no):
            new_l.append(word)
    print(new_l)


filter_long_words(l, number)

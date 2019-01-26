l = "scaksjlajidajfiajljdldkj"
li = []
new_li = []
for i in l:
    li.append(i)
length = len(li)
print(length)
for j in range(length):
    for k in range(j+1, length):
        if(li[j]==li[k]):
            new_li.append(li[j])
print(new_li)
print(len(new_li))
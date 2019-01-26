word = 'a'
replace = 'b'
sentence = 'This is a sentence'
split_values = []
tmp = ''
for c in sentence:
    if c == ' ':
        split_values.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_values.append(tmp)

for n, i in enumerate(split_values):
    print(i)
    if i==word:
        split_values[n]=replace
    #split_values.append(i)
print(split_values)
#print(''.join(split_values))
'''string = 'The quick brown fox jusmps over the lazy dog'
# Define your variables
result = ''
for i in string:
        if i == 'o':
            i = '0'
        result += i
print(result)'''
def c_replaced(arg1, arg2, arg3):
    split_values = []
    tmp = ''
    new_tmp = ''
    rev_word = ''
    # with out using .split()
    for c in arg1:
        if c == ' ':
            split_values.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        split_values.append(tmp)

        # reverse with out using reverse()
    for k in arg3:
        rev_word = k+rev_word

    # with out using replace()
    for n, i in enumerate(split_values):
        if i == arg2:
            split_values[n] = rev_word
    for j in split_values:
        new_tmp += j+" "
    return new_tmp


main_string = 'Marry had a little lamb.'
change_this = 'little'
change_with = 'big'
replaced_string = c_replaced(main_string, change_this, change_with)
print(replaced_string)

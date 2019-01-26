number = int(input("enter the number you want:-"))
col = int(input("enter the col number:-"))


def Series(n, m):
    str_n = str(n)
    sums = n
    sum_str = str(n)
    for i in range(1, m):
        sum_str = sum_str + str_n
        sums = sums + int(sum_str)

    return sums
totall = Series(number,col)
print(totall)

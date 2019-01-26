def pattrn(n):
    num = 1
    for i in range(0, 5):
        for j in range(5, i, -1):
            print(num, end=" ")
            num = num+1
        print()
        num = 1
pattrn(5)

def pat(n):
    num = 1
    incr = 1
    for i in range(0, 5):
        for j in range(0, incr):
            print(num, end=" ")
            num = num+1
        print()
        incr = incr + 2
pat(5)

def patrn(n):
    num = 1
    count = 0
    decr = n*2 - 2
    for i in range(0, 5):
        for k in range(0, decr):
            print(end=" ")
        for j in range(0, i):
            count = count+1
        num = count
        temp = num
        for j in range(0, i):
            print(num, end=" ")
            num = num-1
        print()
        num = temp
        decr = decr -2
patrn(5)
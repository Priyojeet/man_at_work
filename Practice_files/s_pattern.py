def pattern(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(val)
            print(ch, end=" ")
            val = val+1
        print()
pattern(5)

def patrn(n):
    val = 65
    for i in range(0, n):
        for j in range(0, i+1):
            ch = chr(val)
            print(ch, end=" ")
        val = val + 1
        print()
patrn(5)

def pat(n):
    incr = 1
    val = 65
    for i in range(0,n):
        for j in range(0, incr):
            ch = chr(val)
            print(ch, end=" ")
            val = val+1
        incr = incr+2
        print()
pat(5)

decr = 8
count = 64
vsl = 65
for i in range(0, 5):
    for k in range(0, decr):
        print(end=" ")
    for j in range(0, i+1):
        count = count+1
    val = count
    temp = val
    for j in range(0, i+1):
        ch = chr(val)
        print(ch, end=" ")
        val = val-1
    val = temp
    decr = decr - 2
    print()

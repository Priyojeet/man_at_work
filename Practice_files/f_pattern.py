def patrn(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")

patrn(6)

def pat_rot(m):
    k = 2*m - 2
    for i in range(0, m):
        for j in range(0, k):
            print(end=" ")
        k = k-2
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")


pat_rot(6)

def patrn_rev(a):
    k = 4*a - 4
    tim = 1
    for i in range(0, a):
        for j in range(0, k):
            print(end=" ")
        k = k-4
        for j in range(0, tim):
            print("* ", end="")
        tim = tim+2
        print()

patrn_rev(6)


def patrn_new(a):
    k = 1
    for i in range(0,a):
        for j in range(0, k):
            print("* ", end="")
        k = k+2
        print()

patrn_new(6)

def trangle(n):
    k = 2*n -2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k-1
        for j in range(0, i+1):
            print("* ", end="")
        print()

trangle(6)

def u_pattrn(n):
    for i in range(0, n):
        for j in range(n, i, -1):
            print("* ", end="")
        print()
u_pattrn(6)
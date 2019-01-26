def filter(arr, trav, i, x, y):
    c = 0
    arri = arr[i]
    while(arri in trav):
        arri -= 1
        c += 1
        if(x <= c*y):
            return (x, arr[i-1])
    return(c*y, arri)
n,x,y = list(map(int,input().split()))
arr = list(map(int, input().split()))
arr.sort()
l = len(arr)
trav = set()
trav.add(arr[0])

c = 0
for i in range(1, l):
    if(arr[i] in trav):
        if(x<= y):
            c += x
            arr[i] = arr[i-1]
        else:
            ret1 = filter(arr, trav, i, x, y)
            arr[i] = ret1[1]
            trav.add(arr[i])
            c+=ret1[0]
    else:
        trav.add(arr[i])
print(c)
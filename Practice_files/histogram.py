def histogram(items):
    for i in items:
        output = ""
        times = i
        while(times>0):
            output+='*'
            times =times -1
        print(output)
histogram([2,3,6,5])

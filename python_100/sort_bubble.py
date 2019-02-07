# python program for bubble sort

def sort(list):
    for num in range(len(list)-1,0,-1):
        for i in range(num):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [14,46,43,27,57,41,45,21,70]
sort(list)
print(list)
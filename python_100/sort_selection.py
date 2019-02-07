# python program for selection sort

def sort(list):
   for i in range(len(list)-1,0,-1):
       maxpos=0
       for j in range(1,i+1):
           if list[j]>list[maxpos]:
               maxpos = j

       temp = list[i]
       list[i] = list[maxpos]
       list[maxpos] = temp

nlist = [14,46,43,27,57,41,45,21,70]
sort(nlist)
print(nlist)
# python program for insertion sort

def sort(list):
   for i in range(1,len(list)):

     currentvalue = list[i]
     position = i

     while position>0 and list[position-1]>currentvalue:
         list[position]=list[position-1]
         position = position-1

     list[position]=currentvalue

nlist = [14,46,43,27,57,41,45,21,70]
sort(nlist)
print(nlist)
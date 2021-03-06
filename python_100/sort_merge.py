# python program for marge sort

def sort(list):
    print("splitting ", list)
    if len(list)>1:
        mid = len(list)//2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        sort(lefthalf)
        sort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k]=lefthalf[i]
                i=i+1
            else:
                list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            list[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",list)

nlist = [14,46,43,27,57,41,45,21,70]
sort(nlist)
print(nlist)

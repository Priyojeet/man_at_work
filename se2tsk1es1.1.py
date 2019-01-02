import sys

def rev(arg):
	l = len(arg)
	new_list = [None]*l
	for i in arg:
		l = l-1
		new_list[l] = i
	print(new_list)


def list_add(arg):
	result = 0
	for i in arg:
		result=result+i
	print(result)

def myreduce(func, list):
	v = func(list)
	return v

l = []
try:
	len_l = int(input("enter the length of the list you want:-"))
	for i in range(len_l):
		e = int(input("enter the element:-"))
		l.append(e)
except:
	error = sys.exc_info()[0]
	print(error)
myreduce(list_add, l)
myreduce(rev, l)


name = "Priyojeet"
print(name)
print(type(name))


def length(arg):  # custom function which works as like inbuilt len()
    count = 0
    for i in arg:
        count+=1
    return count


l = length(name)
for i in range(l):
    print(name[i])

print(name[0], name[4], name[3])
print(name[:], name[1:], name[:3], name[-1], name[:-1], name[::1], name[::2], name[::-1])  # slicing

# built-in methods

print(name.upper())
print(name.lower())
print(name.split())
print(name.split('r'))
print(name.count('e'))
print(name.find('o'))
print(name.center(20, 'z'))
print(name.isalnum())
print(name.isalpha())
print(name.islower())
print(name.isspace())
print(name.istitle())
print(name.isupper())
print(name.endswith('t'))
print(name.partition('o'))

l = list(name)
print(l)
print(l.pop(1))
print(l)
l.insert(1,'r')
print(l)
l.reverse()
print(l)
l.sort()
print(l)
l.remove('y')
print(l)
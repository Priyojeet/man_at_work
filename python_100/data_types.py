"""Python has five standard data types −

1. Numbers
2. String
3. List
4. Tuple
5. Dictionary"""

# python numbers.
# int

a = 10
print(a)
print('data type of a is:-',type(a))

# float

a = 5.4
print(a)
print('data type of a is:-',type(a))

# complex

a = 5j
print(a)
print("data type of a is:-",type(a))

# python strings

str1 = "Priyojeet"
print(str1)
print('data type of str1 is:-',type(str1))

# python lists

l = [1,3,5,6,'hii','bangalore']
print(l)
print("data type of l is:-",type(l))


# python tuples

t = ('jeet', 420, "on", "lucifer", 999)
print(t)
print("data type of t is:-",type(t))

# dictionary

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
dict1 = {'name': 'jeet','code':999, 'dept': 'fun'}

print(dict)
print(dict1)
print("keys of the dictionary dict are:-",dict.keys())
print("values of the dictionary dict1 are:-",dict1.values())

"""
1.
int(x [,base])

Converts x to an integer. base specifies the base if x is a string.

2	
long(x [,base] )

Converts x to a long integer. base specifies the base if x is a string.

3	
float(x)

Converts x to a floating-point number.

4	
complex(real [,imag])

Creates a complex number.

5	
str(x)

Converts object x to a string representation.

6	
repr(x)

Converts object x to an expression string.

7	
eval(str)

Evaluates a string and returns an object.

8	
tuple(s)

Converts s to a tuple.

9	
list(s)

Converts s to a list.

10	
set(s)

Converts s to a set.

11	
dict(d)

Creates a dictionary. d must be a sequence of (key,value) tuples.

12	
frozenset(s)

Converts s to a frozen set.

13	
chr(x)

Converts an integer to a character.

14	
unichr(x)

Converts an integer to a Unicode character.

15	
ord(x)

Converts a single character to its integer value.

16	
hex(x)

Converts an integer to a hexadecimal string.

17	
oct(x)

Converts an integer to an octal string."""

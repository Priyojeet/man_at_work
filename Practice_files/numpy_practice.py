import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from numpy.random import randint as ri

a = np.array([1, 2, 3])
print(a)
print("dimension", a.shape)
print(a.ndim)
print(np.array([1, 2, 3.0]))

a1 = np.array([[1, 2], [3, 4]])
print(a1)
print(a1.ndim)

print(np.array([1,2,3], ndmin=2))
print(np.array([1,2,3], dtype=complex))

x = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i2')])
print(x)
print(x['a'])
print(type(x['b']))
print(x['b'])
print(type(x['a'][0]))
print(type(x['b'][0]))

# creating array from sub-class
x = np.array(np.mat('1 2; 3 4'))
print(x)
print(type(x))
x = np.array(np.mat('1 2; 3,4'), subok=True)
print(x)
print(type(x))

# numpy.asarray
a = [1,2]
a_a = np.asarray(a)
print(a_a)
print(np.asarray(a) == a_a)
a = np.array([1, 2], dtype=np.float32)
print(a)
print(np.asarray(a, dtype=np.float32) is a)
print(np.asarray(a, dtype=np.float64) is a)

print(issubclass(np.matrix, np.ndarray))
print(issubclass(np.ndarray, np.matrix))

a = np.matrix([[1, 2]])
print(np.asanyarray(a) is a)
print(np.asarray(a) is a)

# numpy.asanyarray

a = [1,2]
a_x = np.asanyarray(a)
print(a_x)
print(type(a_x))
a = np.matrix([1,2])
b = np.asanyarray(a)
print(b is a)
print(type(a))
print(type(b))
print(np.array(a, copy=True))
x = np.array([1,2,3])
y = x
z = np.copy(x)

x[0] = 10
print(x[0] == y[0])
print(x[0] == z[0])

x = np.fromfunction(lambda i, j:i+j, (3, 3), dtype=int)
print(x)
x = np.fromfunction(lambda i, j: i==j, (3, 3), dtype=int)
print(x)

iterable = (x*x for x in range(5))
print(iterable)
print(np.fromiter(iterable, float))
print(np.fromstring('1 2', dtype=int, sep=' '))
print(np.fromstring('1,2', dtype=int, sep=','))

# load data from a text file

c = StringIO('0 1\n2 3')
print(np.loadtxt(c))
d = StringIO('M 21 72\nF 35 58')
result = np.loadtxt(d, dtype={'names':('gender', 'age', 'weight'), 'formats':('S1','i4','f4')})
print(result)

c = StringIO('1, 0, 2\n3, 0, 4')
x, y = np.loadtxt(c, delimiter=',', usecols=(0, 2), unpack=True)
print(x,y)

x1 = np.array([1,2,3,4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
r = np.core.records.fromarrays([x1,x2,x3], names='a,b,c')
print(r)
print(r[1])
print(x1[1])
print(r.a)
x1[1] = 34
print(r.a)
print(x1[1])

# data types
l_m = [1,2,3]
arr = np.array(l_m)
arr1 = np.mat(l_m)
arr2 = np.asarray(l_m)
arr3 = np.asanyarray(l_m)
print(type(arr), type(arr1), type(arr2), type(arr3))
print("vectors are :-", arr)

mat = [[1,2,3], [4,5,6],[7,8,9]]
matrix = np.array(mat)
print('type of this matrix is:-', type(matrix))
print("the matrix is:-", matrix)
print('dimension of the matrix is:-', matrix.ndim, sep='')
print('size of the matrix is:-', matrix.size,sep='')
print('shape of the matrix is:-', matrix.shape, sep='')
print('data type of the matrix is:-', matrix.dtype, sep='')

mat = [[1.2, 3,4],[1,3.4, 5],[1,3,5.6]]
matrix = np.array(mat)
print("data type of this matrix is:-",matrix.dtype, sep='')

# matrix made from tuples
b = np.array([(1.3, 3,4),(4,5,6)])
print(b)
print("data type of this matrix is:-", b.dtype, sep='')

# arange and linspace

print("A series of numbers:", np.arange(5,16))
print("numbers r in 2 step skipped:-", np.arange(0, 11, 2))
print("numbers r in skipped by a float number:-",np.arange(0,11,2.5))
print("every 5th number from 50 in reverse:-", np.arange(50,0,-5))
print("linearly separated numbers from a given renge:-", np.linspace(1,5,21))

# matrix creation

print("vector of zeros:-")
print(np.zeros(5))
print("matrix of zeros:-\n", np.zeros((3,4)))
print("vector of ones:-\n", np.ones(5))
print("matrix of ones:-\n", np.ones((4,5)))
print("matrix of 5's using ones:-\n", 5*np.ones((3,4)))
print("matrix of 5's using ones:-\n", 5*np.ones((3,4), 'i4'))
print("matrix of 5's:-\n", np.empty((3,4)))
mat1 = np.eye(4)  # creation of identity matrix
print("dimension is:-", mat1.shape)
print(mat1)
print(np.arange(3))  # for int
print(np.arange(3.0))  # for float
print(np.arange(3,7))
print(np.arange(3,7,2))
print(np.linspace(2.0, 3.0, 5))
print(np.linspace(2.0, 3.0, num=5))
print(np.linspace(2.0, 3.0, num=5, endpoint=False))
print(np.linspace(2.0, 3.0, 5, endpoint=True))

# for log scale
print(np.logspace(2.0, 3.0, 5))
print(np.logspace(2.0, 3.0, 5, endpoint=False))
print(np.logspace(2.0, 3.0, 5, base=2.0))

x = np.arange(9).reshape((3,3))
print(x)
print(np.diag(x))
print(np.diag(x, k=1))
print(np.diag(x, k=-1))
print(np.diag(np.diag(x)))

# Create a two-dimensional array with the flattened input as a diagonal.
print(np.diagflat([[1,2], [3,4]]))
print(np.diagflat([1,2], 1))
# An array with ones at and below the given diagonal and zeros elsewhere.
print(np.tri(3,5,2, dtype=int))
print(np.tri(3,5,-1))

# return a Lower triangle of an array.
print(np.tril([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1))
# return Upper triangle of an array.
print(np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1))

# random number generation

print(np.random.rand(2,3))
print(np.random.randn(4,3))
print(np.random.randint(1, 100, 10))
print(np.random.randint(1, 100, (4,4)))
print(np.random.randint(1, 7, 20))

# Reshaping

print("reshaping starting from here.")
a = ri(1,100, 30)
b = a.reshape(2,3,5)
c = a.reshape(6,5)
print(a, a.shape,"\n", b, b.shape,"\n", c, c.shape)

A = ri(1,100,10)
print(A)
print("sorted vector:-", np.sort(A, kind='mergesort'))

M = ri(1,100,25).reshape(5,5)
print(np.sort(M, kind='mergesort'))     # default axis is always 1
print("for row:-\n",np.sort(M, axis=1, kind='margesort'))
print("for col:-\n",np.sort(M, axis=0, kind='margesort'))

print(a.max())
print(M.max())

print("max of location:", a.argmax())
print("max of location:", M.argmax())

# Indexing and Slicing

arr = np.arange(0,11)
print("Array:", arr)
print("element at 4th index is:", arr[4])
print("elements from 3rd to 5th index are :-", arr[3:6])
print("elements up to 4th index:-", arr[:4])
print("elements up to 4th index:-", arr[4:])
print("elements in reverse:-",arr[-1::-1])
print("last 3 elements:- ", arr[-1:-6:-2])

arr = np.arange(0,21,2)
print("new arr:-", arr)
print("elements at 2nd, 4th, 9th:-", arr[[2,4,9]])

mat = np.array(ri(10,100,15)).reshape(3,5)
print(mat)
print(mat[1][2],":-element from (1,2) co-ordinates")
print(mat[1,2],":-element from (1,2) co-ordinates")
print("elements from 2nd row:-", mat[2])
print("elements from 2nd col:-", mat[:,2])
print("Matrix with row indices 1 and 2 and column indices 3 and 4\n", mat[1:3,3:5])
print("Matrix with row indices 0 and 1 and column indices 1 and 3\n", mat[0:2,[1,3]])

# Slicing

mat = np.array([[11,12,13],[21,22,23],[31,32,33]])
print(mat)

mat_slice = mat[:2, :2]
print(mat_slice)
mat_slice[0,0] = 1000
print(mat_slice)
print(mat)

mat = np.array([[11,12,13],[21,22,23],[31,32,33]])
print(mat)
mat_slice = np.array(mat[:2, :2])
print(mat_slice)
mat_slice[0,0] = 1000
print(mat_slice)
print(mat)

# universal Function
mat1 = np.array(ri(1,10,9)).reshape(3,3)
mat2 = np.array(ri(1,10,9)).reshape(3,3)
print(mat1,"\n",mat2)
print("Addition is:-\n", mat1+mat2)
print("multiplication is:-\n", mat1*mat2)
print("Division is:-\n", mat1/mat2)
print("leaner combination is:-\n", 3*mat1-2*mat2)
print("addition of a scalar:-\n", 100+mat1)
print("exponentiation of matrix cubed:-\n", mat1**3)
print("exponentiation of sq-root:-\n", pow(mat1,0.5))

# broadcasting
start = np.zeros((4,3))
print(start)
add_row = np.array([1,2,0])
print(add_row)
y = start+add_row
print(y)
add_cols = np.array([[0,1,2,3]])
add_cols = add_cols.T
print(add_cols)
y = start +add_cols
print(y)

add_scalar = np.array([100])
print(start+add_scalar)

# Array Math

mat1 = np.array(ri(1,10,9)).reshape(3,3)
mat2 = np.array(ri(1,10,9)).reshape(3,3)

print("Sq-root is:-\n", np.sqrt(mat1))
print("Exponential power:-\n", np.exp(mat1))
print("10-base log of a matrix:-\n", np.log10(mat1))
print("modulo reminder :-\n", np.fmod(mat1,mat2))
A = np.linspace(0,12*np.pi, 1001)
print(A)

plt.scatter(x=A, y=100*np.exp(-A/10)*(np.sin(A)))
plt.title("ha ha ha, I'm playing")
plt.show()
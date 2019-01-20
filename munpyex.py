import numpy as np


print(np.zeros(10))
print(np.ones(10))
print(5*np.ones(10))
print(np.arange(10,50))
print(np.arange(10,50,2))
print(np.arange(1,9+1).reshape(3,3))
print(np.eye(3,3))
print(np.random.random())
print(np.random.random(25))
print(np.random.randn(10,10))
print(np.linspace(0,1,20))

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[2:, 1:])
print(mat[3, 4])
print(mat[0:3,1:2])
print(mat[4])
print(mat[3:])
print(np.sum(mat))
print(np.std(mat))
print(np.sum(mat, axis=0))


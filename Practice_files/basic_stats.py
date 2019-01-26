import matplotlib.pyplot as plt
from numpy.random import randint as ri
import numpy as np

mat1 = np.array(ri(1,10,9)).reshape(3,3)
mat2 = np.array(ri(1,10,9)).reshape(3,3)
print("\n1st Matrix of random single-digit numbers\n","-"*50,"\n",mat1)
print("\n2nd Matrix of random single-digit numbers\n","-"*50,"\n",mat2)

print("\nSum of all numbers in 1st matrix\n","-"*50,"\n",np.sum(mat1))
print("\nSum of all numbers in columns of 1st matrix\n","-"*50,"\n",np.sum(mat1,axis=0))

print("\nSum of all numbers in rows of 1st matrix\n","-"*50,"\n",np.sum(mat1,axis=1))
print("\nProduct of all numbers in rows of 1st matrix\n","-"*50,"\n",np.prod(mat1,axis=1))

print("\nProduct of all numbers in columns of 2nd matrix\n","-"*50,"\n",np.prod(mat2,axis=0))
print("\nMean of all numbers in 1st matrix\n","-"*50,"\n",np.mean(mat1))

print("\nStandard deviation of all numbers in 1st matrix\n","-"*50,"\n",np.std(mat1))

mat1 = np.array(ri(1,100,9)).reshape(3,3)
print("\nModified matrix of random numbers from 1 to 99\n","-"*50,"\n",mat1)

print("\nStandard deviation of all numbers in the modified matrix, a larger number\n","-"*80,"\n",np.std(mat1))

print("\nVariance of all numbers in the modified matrix, a larger number\n","-"*80,"\n",np.var(mat1))

print("\nMedian of all numbers in the modified matrix\n","-"*60,"\n",np.median(mat1))

mat2 = np.array(ri(1,100,50)).reshape(10,5)
print(mat2)
print("\nStandard deviation along the columns in the modified matrix\n","-"*60,"\n",np.std(mat2,axis=0))

mat1 = np.array(ri(1,100,20)).reshape(4,5)
print(mat1)
print("\nFlattened and sorted matrix (as vector)\n","-"*50,"\n",np.sort(mat1.reshape(1,20)))
print("\n50th percentile of all numbers in the modified matrix\n","-"*60,"\n",np.percentile(mat1,50))
print("\n90th percentile of all numbers in the modified matrix\n","-"*60,"\n",np.percentile(mat1,90))


print("Correlation")

A = ri(1,5,20) # 20 random integeres from a small range (1-10)
B = 2*A+5*np.random.randn(20) # B is twice that of A plus some random noise
print("\nB is twice that of A plus some random noise")

plt.scatter(A,B) # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a small positive correlation")
plt.show()

print(np.corrcoef(A,B))  # Correleation coefficient matrix between A and B

A = ri(1,50,20)  # 20 random integeres from a larger range (1-50)
B = 100-2*A+10*np.random.randn(20)  # B is 100 minus twice that of A plus some random noise
print("\nB is 100 minus twice that of A plus some random noise")
plt.scatter(A,B)  # Scatter plot of B
plt.title("Scatter plot of A vs. B, expect a large negative correlation")
plt.show()
print("")
print(np.corrcoef(A,B))  # Correleation coefficient matrix between A and B

print("Linear Algebra Using Numpy")

A = np.arange(1,10).reshape(3,3)
B = ri(1,10,9).reshape(3,3)
print("\n1st Matrix of 1-9 single-digit numbers (A)\n","-"*50,"\n",A)

print("\n2nd Matrix of random single-digit numbers (B)\n","-"*50,"\n",B)
print("\nDot product of A and B (for 2D arrays it is equivalent to matrix multiplication) \n","-"*80,"\n",np.dot(A,B))

A = np.arange(1,6)
B = ri(1,10,5)

print("\n1st Vector of 1-5 numbers (A)\n","-"*50,"\n",A)
print("\n2nd Vector of 5 random single-digit numbers (B)\n","-"*50,"\n",B)
print("\nInner product of vectors A and B \n","-"*50,"\n",np.inner(A,B), "(sum of all pairwise elements)")
print("\nOuter product of vectors A and B \n","-"*50,"\n",np.outer(A,B))

print("matrix transpose and matrix inverse")

A = ri(1,10,9).reshape(3,3)
print(A)
print("\n3x3 Matrix of random single-digit numbers\n","-"*50,"\n",A)
print("\nMatrix transpose\n","-"*50,"\n",np.transpose(A))

B = ri(1,10,6).reshape(3,2)
print(B)

print("\n3x2 Matrix of random single-digit numbers\n","-"*50,"\n",B)
print("\n2x3 Matrix transpose\n","-"*50,"\n",np.transpose(B))
print("\nMatrix multiplication of B and B-transpose\n","-"*50,"\n",np.dot(B, np.transpose(B)))

A = ri(1,10,16).reshape(4,4)
print(A)
print("\n4x4 Matrix of random single-digit numbers\n","-"*50,"\n",A)
print("\nMatrix trace\n","-"*50,"\n",np.trace(A))
print("\nMatrix trace with ofset +1 (upper triangle)\n","-"*50,"\n",np.trace(A,offset=1))
print("\nMatrix trace with ofset -1 (lower triangle)\n","-"*50,"\n",np.trace(A,offset=-1))
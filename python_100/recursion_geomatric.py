# program to calculate the geometric sum of n-1.

def sum(r, n):
   if n < 2:
       return 1
   else:
       geoSum = r**(n-1)
   geoSum += sum(r, n-1)
   return geoSum

print(sum(2,7))

# Python program to calculate the harmonic sum of n-1

def sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (sum(n - 1))


print(sum(7))
import numpy as np
from numpy import convolve

def move(arg, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(arg, weights, 'valid')
    return sma
x = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window = 3
print(move(x,window))
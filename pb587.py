import math
import time
import scipy.integrate as integrate


def aire(w, x):
    return w*x**2/2+integrate.quad(lambda u: 1-math.sqrt(2*u-u**2), x, 1)[0]


def solve():
    aire_tot = 1-math.pi/4
    ratio = 1
    n = 1
    while ratio > 0.001:
        w = 1/n
        x = (w+1-math.sqrt(2*w))/(1+w**2)
        ratio = aire(w, x)/aire_tot
        n += 1
    return n-1

start = time.perf_counter()
print(solve())
print('temps d execution', time.perf_counter() - start, 'sec')

import time
import math


def solve(h0, v, g):
    a = -g/(2*v**2)
    b = (v**2)/(2*g)+h0
    return round(-(math.pi*b**2)/(2*a), 4)


start = time.perf_counter()
print(solve(100, 20, 9.81))
print('temps d\'exécution', time.perf_counter() - start, 'sec')

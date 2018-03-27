import math
import time
import numba


@numba.jit(nopython=True)
def isqrt(n):
    xn = 1
    xn1 = (xn + n//xn)//2
    while abs(xn1 - xn) > 1:
        xn = xn1
        xn1 = (xn + n//xn)//2
    while xn1*xn1 > n:
        xn1 -= 1
    return int(xn1)


@numba.jit(nopython=True)
def n(r):
    res = 1 + 4*int(r)
    for i in range(1, int(r)+1):
        res += 4*isqrt(r**2-i**2)
    return res


@numba.jit(nopython=True)
def solve(r):
    return (3*r**2)//2+n(r/(4*math.sqrt(2)))-76-r//4+1


start = time.perf_counter()
print(solve(10**9))
print('temps d\'exécution', time.perf_counter() - start, 'sec')

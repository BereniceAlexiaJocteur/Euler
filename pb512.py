import time
import numpy


def init_phi(n):
    phi = numpy.empty(n//2, dtype='int64')
    for i in range(n//2):
        phi[i] = 2*i+1
    for p in range(1, n//2):
        pi = 2*p+1
        if phi[p] == pi:
            pii = 2*p
            phi[p] = pii
            for i in range(p+pi, n//2, pi):
                phi[i] = (phi[i]//pi)*pii
    return phi


def solve(n):
    phi = init_phi(n)
    res = 1
    for i in range(1, len(phi)):
        res += phi[i]
    return res


start = time.perf_counter()
print(solve(5*10**8))
print('temps d\'exécution', time.perf_counter() - start, 'sec')

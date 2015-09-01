# -------------------------------------------------------------------------------
# Name:        pb351
# Purpose:     project euler
# Created:     27/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def phi_sieve(lim):
    limit = lim + 1
    visited = [False] * limit
    phi = [i for i in range(limit)]
    for i in range(2, limit):
        if not visited[i]:
            phi[i] = i-1
            for j in range(i + i, limit, i):
                phi[j] = phi[j]//i * (i-1)
                visited[j] = True
    del visited
    return phi


def h(n):
    phi = phi_sieve(n)
    res = n * (n+1) // 2
    for k in range(n+1):
        res -= phi[k]
    return 6 * res


def main():
    start = time.perf_counter()
    print(h(100000000))
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
# -------------------------------------------------------------------------------
# Name:        pb204
# Purpose:     project euler
# Created:     30/08/2015
# -------------------------------------------------------------------------------

import primes
import sys
import time


class Problem():

    def __init__(self, typ, limit):
        self.type = typ
        self.limit = limit
        self.list_primes = primes.primes(typ)
        self.nb_primes = len(self.list_primes)

    def fonction(self, n, lvl, lim, deptlim):
        if lvl == deptlim:
            return 1
        if n > lim:
            return 0
        return self.fonction(n*self.list_primes[lvl], lvl, lim, deptlim) + self.fonction(n, lvl+1, lim, deptlim)

    def solve(self):
        print(self.fonction(1, 0, self.limit, self.nb_primes))


def main():
    start = time.perf_counter()
    u = Problem(100, 10**9)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
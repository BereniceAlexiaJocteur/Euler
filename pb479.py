# -------------------------------------------------------------------------------
# Name:        pb479
# Purpose:     project euler
# Created:     03/10/2015
# -------------------------------------------------------------------------------

# I used relations between roots and coefficients and the little Fermat's Theorem

import time
import sys


class Problem():

    def __init__(self, n, m):
        self.n = n
        self.mod = m
        self.res = 0

    def get_res(self):
        for i in range(2, self.n + 1):
            self.res = (self.res + (pow(1 - i * i, self.n + 1, self.mod) - (1 - i * i)) * pow(-i * i, self.mod - 2,  self.mod) % self.mod) % self.mod

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(10**6, 1000000007)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
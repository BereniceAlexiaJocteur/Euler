# -------------------------------------------------------------------------------
# Name:        pb487
# Purpose:     project euler
# Created:     03/10/2015
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, u, k):
        self.u = u
        self.k = k
        self.divs = None

    def num_divisor_sieve(self, n):
        self.divs = [1] * (n + 1)
        self.divs[0] = 0
        for i in range(2, n + 1):
            for j in range(i, n + 1, i):
                self.divs[j] += 1

    def m(self, n, k):
        return max(self.divs[n:n+k])

    def s(self, u, k):
        som = self.m(1, k)
        currmax = self.m(1, k)
        temp0 = self.divs[1]
        for i in range(2, u - k + 2):
            temp1 = self.divs[i+k-1]
            if temp1 > currmax:
                currmax = temp1
            elif temp0 == currmax:
                currmax = self.m(i, k)
            som += currmax
            temp0 = self.divs[i]
        return som

    def solve(self):
        self.num_divisor_sieve(self.u)
        print(self.s(self.u, self.k))


def main():
    start = time.perf_counter()
    u = Problem(10**8, 10**5)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

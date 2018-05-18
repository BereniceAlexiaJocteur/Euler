# -------------------------------------------------------------------------------
# Name:        pb380
# Purpose:     project euler
# Created:     06/02/2016
# -------------------------------------------------------------------------------

import math
import time
import sys


class Problem():

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.res = 0

    def solve(self):
        for k in range(1, self.n):
            b = 4*math.sin(k*math.pi/(2*self.n))**2
            for h in range(1, self.m):
                a = 4*math.sin(h*math.pi/(2*self.m))**2
                self.res += math.log10(b+a)
        u = int(self.res)
        v = round(pow(10, self.res-u), 4)
        print(str(v)+'e'+str(u))


def main():
    start = time.perf_counter()
    u = Problem(100, 500)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

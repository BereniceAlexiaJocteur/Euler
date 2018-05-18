# -------------------------------------------------------------------------------
# Name:        pb235
# Purpose:     project euler
# Created:     09/02/2016
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self):
        self.precision = 1
        self.target = -2*10**11

    @staticmethod
    def s(r):
        somme = 0
        for i in range(1, 5001):
            somme += (300-i)*r**(i-1)
        return somme

    def solve(self):
        rd = 0.1
        r = 1
        a = 0
        while abs(a - self.target) > self.precision:
            a = self.s(r)
            if a > self.target:
                r += rd
            else:
                r -= rd
            rd /= 2
        print(round(r, 12))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

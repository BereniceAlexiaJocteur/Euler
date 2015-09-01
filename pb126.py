# -------------------------------------------------------------------------------
# Name:        pb126
# Purpose:     project euler
# Created:     31/08/2015
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n
        self.lim = 18523
        self.list_cubes = [0] * (self.lim + 1)

    def fill_list(self):
        for a in range(1, self.lim):
            if 6*a**2 > self.lim:
                break
            for b in range(a, self.lim):
                ab = a * b
                if 2*b*(2*a+b) > self.lim:
                    break
                for c in range(b, self.lim):
                    if 2*(ab+a*c+b*c) > self.lim:
                        break
                    lvl = 1
                    nb_cubes = self.fonction_c(a, b, c, lvl)
                    while nb_cubes < self.lim:
                        self.list_cubes[nb_cubes] += 1
                        lvl += 1
                        nb_cubes = self.fonction_c(a, b, c, lvl)

    @staticmethod
    def fonction_c(a, b, c, lvl):
        return 2*(a*b + a*c + b*c) + 4*(lvl-1)*(a+b+c+lvl-2)

    def inv_c(self):
        for i in range(1, self.lim+1):
            if self.list_cubes[i] == self.n:
                return i
        return None

    def solve(self):
        self.fill_list()
        print(self.inv_c())


def main():
    start = time.perf_counter()
    u = Problem(1000)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
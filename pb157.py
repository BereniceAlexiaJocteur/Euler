# -------------------------------------------------------------------------------
# Name:        pb157
# Purpose:     project euler
# Created:     09/09/2015
# -------------------------------------------------------------------------------

import fractions
import math
import sympy
import time
import sys


class Problem():

    def __init__(self, n):
        self.lim = n
        self.pwrs2 = [2 ** k for k in range(int(math.log(2 * 10 ** self.lim, 2)) + 1)]
        self.pwrs5 = [5 ** k for k in range(int(math.log(2 * 10 ** self.lim, 5)) + 1)]

    def num_sol(self, n):
        products = [a * b for a in self.pwrs2 for b in self.pwrs5 if a * b <= 2 * 10 ** n]
        candidates = [(a, b) for a in products for b in products if
                      a <= b and ((b + a) * 10 ** n) % (a * b) == 0 and fractions.gcd(a, b) == 1]
        listp = [((a + b) * 10 ** n) // (a * b) for a, b in candidates]
        resu = 0
        for a in listp:
            resu += sympy.divisor_count(a)
        return resu

    def solve(self):
        rsufinal = 0
        for w in range(1, self.lim + 1):
            rsufinal += self.num_sol(w)
        print(rsufinal)


def main():
    start = time.perf_counter()
    u = Problem(9)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

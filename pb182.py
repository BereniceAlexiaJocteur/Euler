# -------------------------------------------------------------------------------
# Name:        pb182
# Purpose:     project euler
# Created:     30/08/2015
# -------------------------------------------------------------------------------

import time
import fractions
import sys


class Problem():

    def __init__(self, p, q):
        self.p1 = p - 1
        self.q1 = q - 1
        self.phi = self.p1 * self.q1
        self.somme = 0

    def get_somme(self):
        for e in range(11, self.phi, 12):
            if fractions.gcd(e, self.phi) != 1:
                continue
            e1 = e - 1
            if fractions.gcd(e1, self.p1) == 2 and fractions.gcd(e1, self.q1) == 2:
                self.somme += e
        return self.somme

    def solve(self):
        print(self.get_somme())


def main():
    start = time.perf_counter()
    u = Problem(1009, 3643)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
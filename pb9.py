# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import math
import fractions


class Problem():

    def __init__(self, s):
        self.s2 = s // 2
        self.lim = int(math.sqrt(self.s2))

    def get_triplet(self):
        for m in range(2, self.lim):
            if self.s2 % m == 0:
                sm = self.s2 // m
                while sm % 2 == 0:
                    sm //= 2
                if m % 2 == 1:
                    k = m + 2
                else:
                    k = m + 1
                while k < 2*m and k <= sm:
                    if sm % k == 0 and fractions.gcd(k, m) == 1:
                        d = self.s2 // (k * m)
                        n = k - m
                        a = d * (m**2 - n**2)
                        b = 2 * d * m * n
                        c = d * (m**2 + n**2)
                        return a, b, c
                    k += 2

    def get_prod(self):
        t = self.get_triplet()
        prod = 1
        for i in t:
            prod *= i
        return prod

    def solve(self):
        print(self.get_prod())


def main():
    start = time.perf_counter()
    u = Problem(1000)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
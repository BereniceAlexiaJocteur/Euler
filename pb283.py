# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import fractions
import time
import sys
import sympy
import math


# http://forumgeom.fau.edu/FG2007volume7/FG200718.pdf
class Problem():

    def __init__(self):
        self.triangles = set()
        self.somme = 0

    def get_sum(self):
        for m in range(1, 1001):
            for u in sympy.divisors(2*m):
                for v in range(1, 1+int(u*math.sqrt(3))):
                    if fractions.gcd(u, v) != 1:
                        continue
                    n = 4*m**2*(u**2+v**2)
                    for d1 in sympy.divisors(n):
                        if d1**2 > n:
                            break
                        d2 = n // d1
                        mu = 2*m*u
                        mv = 2*m*v
                        mu1 = mu + d1
                        mu2 = mu + d2
                        if mu1 % v == 0 and mu2 % v == 0:
                            a = mu1//v + mv//u
                            b = mu2//v + mv//u
                            c = (mu1+mu2)//v
                            tri = tuple(sorted([a, b, c]))
                            if tri not in self.triangles:
                                self.triangles.add(tri)
                                self.somme += a+b+c

    def solve(self):
        self.get_sum()
        print(self.somme)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

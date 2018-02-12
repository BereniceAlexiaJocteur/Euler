# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import sympy
import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n

    @staticmethod
    def get_triangle(n):
        return n*(n+1)//2

    def get(self):
        i = 1
        t = self.get_triangle(i)
        while sympy.divisor_count(t) < self.n:
            i += 1
            t = self.get_triangle(i)
        return t

    def solve(self):
        print(self.get())


def main():
    start = time.perf_counter()
    u = Problem(500)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
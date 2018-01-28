# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, lim):
        self.lim = lim
        self.somme = 0

    def get_somme(self):
        b = 2
        c = 3
        while b < self.lim:
            self.somme += b
            a = b + c
            b = a + c
            c = a + b
        return self.somme

    def solve(self):
        print(self.get_somme())


def main():
    start = time.perf_counter()
    u = Problem(4*10**6)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
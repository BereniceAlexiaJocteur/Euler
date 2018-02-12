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
        for i in range(1, self.lim):
            if i % 3 == 0 or i % 5 == 0:
                self.somme += i
        return self.somme

    def solve(self):
        print(self.get_somme())


def main():
    start = time.perf_counter()
    u = Problem(1000)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
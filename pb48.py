# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n, l):
        self.lim = n + 1
        self.l = l

    def get_sum(self):
        somme = 0
        for i in range(1, self.lim):
            somme += pow(i, i, 10**self.l)
        return somme % 10**self.l

    def solve(self):
        print(self.get_sum())


def main():
    start = time.perf_counter()
    u = Problem(1000, 10)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self):
        self.lim = 40586
        self.fact = []

    def init_fact(self):
        f = 1
        self.fact.append(f)
        for i in range(1, 10):
            f *= i
            self.fact.append(f)

    def sum_factoral_digits(self, n):
        somme = 0
        while n > 0:
            temp, n = n % 10, n // 10
            somme += self.fact[temp]
        return somme

    def get_sum(self):
        somme = 0
        for i in range(3, self.lim):
            if i == self.sum_factoral_digits(i):
                somme += i
        return somme

    def solve(self):
        self.init_fact()
        print(self.get_sum())


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
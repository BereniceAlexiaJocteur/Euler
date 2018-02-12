# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n
        self.lim = 194980
        self.pow_digits = []

    def init_pow_digits(self):
        f = 0
        self.pow_digits.append(f)
        for i in range(1, 10):
            f = i**self.n
            self.pow_digits.append(f)

    def sum_pow_digits(self, n):
        somme = 0
        while n > 0:
            temp, n = n % 10, n // 10
            somme += self.pow_digits[temp]
        return somme

    def get_sum(self):
        somme = 0
        for i in range(10, self.lim):
            if i == self.sum_pow_digits(i):
                somme += i
        return somme

    def solve(self):
        self.init_pow_digits()
        print(self.get_sum())


def main():
    start = time.perf_counter()
    u = Problem(5)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
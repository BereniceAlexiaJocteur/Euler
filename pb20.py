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
        self.fact = 1

    def get_factorial(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * self.get_factorial(n-1)

    @staticmethod
    def get_sum_digits(n):
        s = str(n)
        somme = 0
        for i in s:
            somme += int(i)
        return somme

    def solve(self):
        self.fact = self.get_factorial(self.n)
        print(self.get_sum_digits(self.fact))


def main():
    start = time.perf_counter()
    u = Problem(100)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
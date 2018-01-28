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

    @staticmethod
    def sum_digits(n):
        s = str(n)
        somme = 0
        for i in s:
            somme += int(i)
        return somme

    def solve(self):
        p = pow(2, self.n)
        print(self.sum_digits(p))


def main():
    start = time.perf_counter()
    u = Problem(1000)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
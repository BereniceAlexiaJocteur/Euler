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
        self.sum = 0

    def init_sum(self):
        f = open("p13_numbers.txt")
        for line in f:
            self.sum += int(line.strip('\n'))

    def solve(self):
        self.init_sum()
        s = str(self.sum)[:self.n]
        print(s)


def main():
    start = time.perf_counter()
    u = Problem(10)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
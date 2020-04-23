import time
import sys
import math


class Problem():

    def __init__(self):
        self.lobound = math.log10(1.23)
        self.upbound = math.log10(1.24)
        self.count = 0
        self.i = 0
        self.log10_2 = math.log10(2)

    def get_dec_part(self, j):
        logj = self.log10_2*j
        diff = logj - int(logj)
        return diff

    def get_res(self):
        while self.count < 678910:
            self.i += 1
            diff = self.get_dec_part(self.i)
            if self.lobound <= diff < self.upbound:
                self.count += 1

    def solve(self):
        self.get_res()
        print(self.i)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

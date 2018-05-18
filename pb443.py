import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def g(self):
        g = 13
        for n in range(5, self.n + 1):
            w, a, b = self.egcd(n, g)
            g = (b + 1) * g + a * n
        return g

    def solve(self):
        print(self.g)


def main():
    start = time.perf_counter()
    u = Problem(10**9)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
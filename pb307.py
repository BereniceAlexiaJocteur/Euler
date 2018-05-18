import time
import sys
import eulerfun


class Problem():

    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.denominateur = k ** n
        self.proba = 0

    def get_proba(self):
        for i in range(self.k//2 + 1):
            prod = eulerfun.binomial(self.n, i)
            last = self.n - 2 * i + 1
            for j in range(last, self.n+1):
                prod *= j
            prod = prod / (self.denominateur * 2**i)
            self.proba += prod

    def solve(self):
        self.get_proba()
        print(self.proba)


def main():
    start = time.perf_counter()
    u = Problem(3, 7)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

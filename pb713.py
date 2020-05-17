import time
import sys


class Problem():  # A078567

    def __init__(self):
        self.n = 10**7
        self.res = 0

    def get_res(self):
        for i in range(1, self.n):
            for j in range(1, int((self.n-1)/i)+1):
                self.res += self.n - i*j

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

import time
import sys


class Problem():

    def __init__(self):
        self.N = 10**10
        self.N2 = self.N**2
        self.M = 4000
        self.res = 0

    def get_res(self):
        self.res = self.N / 2
        for i in range(1, self.N//2+1):
            item_raised_power_M = 1-(4*i*(self.N-i+1)-2)/self.N2
            if item_raised_power_M > 0.98:
                self.res += item_raised_power_M**self.M

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

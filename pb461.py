import time
import sys
import math


class Problem():

    def __init__(self, n):
        self.n = n
        self.list_f = []
        self.list_double_f = []

    def get_f(self):
        f = 0
        k = 0
        while f < math.pi:
            self.list_f.append(f)
            k += 1
            f = math.exp(k/self.n)-1

    def get_double_f(self):
        for i in range(len(self.list_f)):
            for j in range(len(self.list_f)):
                u = self.list_f[i] + self.list_f[j]
                if u > math.pi:
                    break
                self.list_double_f.append((u, i, j))
        self.list_double_f.sort(key=lambda tup: tup[0])

    def get_res(self):
        return

    def solve(self):
        self.get_f()
        self.get_double_f()
        print(len(self.list_double_f))


def main():
    start = time.perf_counter()
    u = Problem(10000)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
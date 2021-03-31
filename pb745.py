import time
import sys
import math
import numpy as np


class Problem():

    def __init__(self):
        self.n = 10**14
        self.res = 0
        self.mod = 1000000007
        self.sqrt = int(math.sqrt(self.n))
        self.mu = np.array([1 for i in range(self.sqrt + 1)], dtype="int64")
        self.sqrt_sqrt = int(math.sqrt(math.sqrt(self.n)))
        self.list_count_squarefree = dict()

    def init_mu(self):
        for i in range(2, self.sqrt_sqrt+1):
            if self.mu[i] == 1:
                for j in range(i, self.sqrt+1, i):
                    self.mu[j] = self.mu[j]*(-i)
                for j in range(i**2, self.sqrt+1, i**2):
                    self.mu[j] = 0
        for i in range(2, self.sqrt+1):
            if self.mu[i] == i:
                self.mu[i] = 1
            elif self.mu[i] == -i:
                self.mu[i] = -1
            elif self.mu[i] < 0:
                self.mu[i] = 1
            elif self.mu[i] > 0:
                self.mu[i] = -1

    def count_squarefree(self, n):
        if n in self.list_count_squarefree:
            return self.list_count_squarefree[n]
        else:
            res = 0
            sqrt = int(math.sqrt(n))
            for i in range(1, sqrt+1):
                res = (res + (self.mu[i]*int(n/i**2))%self.mod)%self.mod
            self.list_count_squarefree[n] = res
            return res

    def get_res(self):
        for i in range(1, self.sqrt + 1):
            self.res = (self.res+(pow(i, 2, self.mod)*self.count_squarefree(int(self.n/i**2)))%self.mod)%self.mod

    def solve(self):
        self.init_mu()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

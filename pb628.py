import time
import sys


class Problem():

    def __init__(self):
        self.fact_list = [1]
        self.mod = 1008691207
        self.n = 10**8
        self.res = 0

    def init_fact_list(self):
        current_fact = 1
        current_i = 1
        while current_i <= self.n:
            current_fact = (current_fact * current_i) % self.mod
            current_i += 1
            self.fact_list.append(current_fact)

    def get_res(self):
        self.res = self.fact_list[-1] - 1
        for i in range(1, self.n):
            self.res = (self.res + i*self.fact_list[self.n-1-i] - 2*self.fact_list[i]) % self.mod

    def solve(self):
        self.init_fact_list()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
import time
import sys
import math


class Problem():

    def __init__(self):
        self.fibo = [1, 2, 3]
        self.bound = 10**17
        self.sum_z_fibo = [1, 2, 3]
        self.res = 0

    def init_fibo_and_sum_z_fibo(self):
        fn1, fn = 2, 3
        sumzn1, sumzn = 2, 3
        while fn <= self.bound:
            fn1, fn = fn, fn + fn1
            sumzn1, sumzn = sumzn, sumzn + sumzn1 + self.fibo[-2] - 1
            self.fibo.append(fn)
            self.sum_z_fibo.append(sumzn)

    def get_sum(self, x):
        rank = 0
        while self.fibo[rank+1]<=x:
            rank += 1
        remain = x - self.fibo[rank]
        if remain == 0:
            return self.sum_z_fibo[rank]
        return self.sum_z_fibo[rank] + remain + self.get_sum(remain)

    def solve(self):
        self.init_fibo_and_sum_z_fibo()
        self.res = self.get_sum(self.bound-1)
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
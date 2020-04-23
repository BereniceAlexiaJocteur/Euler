import time
import sys


class Problem():

    def __init__(self):
        self.res = 0
        self.fibo = [0, 1]
        self.mod = 1000000007
        self.memo = [0]
        self.old_k = 0

    def init_fibo(self):
        for i in range(89):
            self.fibo.append(self.fibo[-1] + self.fibo[-2])

    def S(self, n):
        k, m = divmod(n, 9)
        print(k)
        if k == 0:
            return sum(range(1, (k+1)))
        resu = ((int(k*'1') % self.mod)*45) % self.mod
        som = self.memo[-1]
        for i in range(self.old_k+1, k):
            som = (som + (int(i*'1') % self.mod)) % self.mod
        self.memo.append(som)
        self.old_k = k
        som = (som * 81) % self.mod
        resu = (resu + som) % self.mod
        resu = (resu + k*9*m) % self.mod
        for i in range(1, m+1):
            resu += i
        resu %= self.mod
        return resu

    def get_res(self):
        for i in range(2, 91):
            print(i)
            self.res = (self.res + self.S(self.fibo[i])) % self.mod

    def solve(self):
        self.init_fibo()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

import time
import sys
import math


class Problem():

    def __init__(self):
        self.res = 0
        self.dr_dic = dict()
        self.mdrs_dic = dict()

    def dr(self, n):
        try:
            return self.dr_dic[n]
        except KeyError:
            u = 1 + ((n-1) % 9)
            self.dr_dic[n] = u
            return u

    def mdrs(self, n):
        maxi = self.dr(n)
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                maxi = max(maxi, self.mdrs_dic[n//i] + self.dr(i))
        self.mdrs_dic[n] = maxi
        return maxi

    def get_res(self):
        for i in range(2, 10**6):
            self.res += self.mdrs(i)

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
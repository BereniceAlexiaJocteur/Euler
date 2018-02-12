# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.mod1 = 50515093
        self.mod2 = 61**10
        self.sn = [290797]
        self.n = 0
        self.res = 0

    def get_sn(self):
        for n in range(self.q):
            self.sn.append(self.sn[n]**2 % self.mod1)

    def get_n(self):
        for n in range(self.q+1):
            tn = self.sn[n] % self.p
            self.n += tn*self.p**n

    def get_res(self):
        i = 1
        temp = self.n // self.p
        while temp > 0:
            self.res += temp % self.mod2
            i += 1
            temp = self.n // self.p**i
        self.res %= self.mod2

    def solve(self):
        self.get_sn()
        self.get_n()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(61, 10**7)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
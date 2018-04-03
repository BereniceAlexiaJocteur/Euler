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
        self.res = 0

    def get_sn(self):
        for n in range(self.q):
            self.sn.append(self.sn[n]**2 % self.mod1)

    def number_of_factor_p_in_factorial_n(self, n):
        div = self.p
        number_of_factors = 0
        curr = n//div
        while curr > 0:
            number_of_factors += curr
            div *= self.p
            curr = n//div
        return number_of_factors

    def get_res(self):
        for i in range(10):
            self.res = (self.res + self.number_of_factor_p_in_factorial_n((self.sn[i] % self.p)*self.p**i)) % self.mod2
        for i in range(10, self.q+1):
            self.res = (self.res + self.number_of_factor_p_in_factorial_n((self.sn[i] % self.p)*self.p**10)) % self.mod2

    def solve(self):
        self.get_sn()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(61, 10**7)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
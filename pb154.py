# -------------------------------------------------------------------------------
# Name:        pb154
# Purpose:     project euler
# Created:     05/09/2015
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, lim, n):
        self.p2 = []
        self.p5 = []
        self.lim = lim
        self.n = n

    @staticmethod
    def sieve_padic_fact(n, p):
        t = [0] * (n+1)
        ind_min = 1
        k = 1
        while p**k <= n:
            i = p**k
            for j in range(ind_min, n+1):
                temp = j//i
                if temp <= 1:
                    ind_min = j
                t[j] += temp
            k += 1
        return t

    def count_coeff(self):
        lim2 = self.p2[self.lim] - self.n
        lim5 = self.p5[self.lim] - self.n
        count = 0

        for a in range(self.lim, (self.lim - 1) // 3, -1):
            a5 = lim5 - self.p5[a]
            a2 = lim2 - self.p2[a]
            for b in range((self.lim - a + 1) // 2, min(a, self.lim - a) + 1):
                c = self.lim - a - b
                if self.p5[b] + self.p5[c] <= a5 and self.p2[b] + self.p2[c] <= a2:
                    if a != b != c:
                        count += 6
                    else:
                        count += 3

        return count

    def solve(self):
        self.p2 = self.sieve_padic_fact(self.lim, 2)
        self.p5 = self.sieve_padic_fact(self.lim, 5)
        print(self.count_coeff())


def main():
    start = time.perf_counter()
    u = Problem(200000, 12)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
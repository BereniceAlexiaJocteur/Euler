# -------------------------------------------------------------------------------
# Name:        pb226
# Purpose:     project euler
# Created:     05/02/2016
# -------------------------------------------------------------------------------

import time
import sys
import math


class Problem():

    def __init__(self):
        self.rounding = 10**(-9)
        self.precision_integration = 47000

    @staticmethod
    def s(x):
        n = int(x)
        return min(x-n, n+1-x)

    @staticmethod
    def circle(x):
        return 0.5-math.sqrt(x*(0.5-x))

    def curve(self, x):
        y = 0
        n = 0
        diff = 1
        while diff > self.rounding:
            prev = y
            y += self.s(x*2**n)/2**n
            diff = y - prev
            n += 1
        return y

    def find_inf_bound(self):
        p = 0
        q = 0.5
        while q - p > self.rounding:
            r = (p+q)/2
            a = self.curve(p) - self.circle(p)
            b = self.curve(r) - self.circle(r)
            if a*b < 0:
                q = r
            else:
                p = r
        return (p+q)*0.5

    def trapezoidal_integration(self, a, b):
        res = 0
        for i in range(self.precision_integration):
            x1 = a+(b-a)*i/self.precision_integration
            x2 = a+(b-a)*(i+1)/self.precision_integration
            f1 = self.curve(x1) - self.circle(x1)
            f2 = self.curve(x2) - self.circle(x2)
            res += (f1+f2)/2*(x2-x1)
        return res

    def solve(self):
        a = self.find_inf_bound()
        b = 0.5
        print(round(self.trapezoidal_integration(a, b), 8))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

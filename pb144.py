# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import math


class Problem():

    def __init__(self):
        self.p = [0.0, 10.1]
        self.q = [1.4, -9.6]
        self.count = 0

    @staticmethod
    def dot_product(u, v):
        return u[0]*v[0] + u[1]*v[1]

    def solve(self):
        while self.q[0] < -0.01 or self.q[0] > 0.01 or self.q[1] < 0:
            norm = 1/math.sqrt(1+self.q[1]**2/(16*self.q[0]**2))
            n = [norm, norm*self.q[1]/(4*self.q[0])]
            prod = self.dot_product(n, [self.p[0]-self.q[0], self.p[1]-self.q[1]])
            r = [-self.p[0]+self.q[0]+2*prod*n[0], -self.p[1]+self.q[1]+2*prod*n[1]]
            t = (-8*r[0]*self.q[0]-2*r[1]*self.q[1])/(4*r[0]**2+r[1]**2)
            a = [t*r[0]+self.q[0], t*r[1]+self.q[1]]
            self.p = self.q
            self.q = a
            self.count += 1
        print(self.count)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, m, n):
        self.result = 1
        self.mod = 7654321776543217
        self.m = m
        self.n = n

    def get_factorial(self):
        for i in range(2, self.m**2 - self.n**2 + 1):
            self.result = (self.result * i) % self.mod

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def get_result(self):
        for i in range(self.m):
            for j in range(self.m):
                if i < self.m - self.n or j < self.m - self.n:
                    if j >= self.m - self.n:
                        x = self.m - self.n - i
                    else:
                        x = self.n - i
                    if i >= self.m - self.n:
                        y = self.m - self.n - j
                    else:
                        y = self.n - j
                    h = x + y - 1
                    self.result = (self.result * self.modinv(h, self.mod)) % self.mod

    def solve(self):
        self.get_factorial()
        print(self.result)
        self.get_result()
        print(self.result)


def main():
    start = time.perf_counter()
    u = Problem(5, 3)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
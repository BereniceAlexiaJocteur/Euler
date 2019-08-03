import time
import sys
import math


class Problem():

    def __init__(self):
        self.res = 0
        self.max = 10**8

    def count_90_degrees(self):
        s = 1
        while 4*s**2 <= self.max:
            r = s+1
            while 2*r*(r+s) <= self.max:
                if math.gcd(r, s) == 1:
                    a = r ** 2 - s ** 2
                    b = 2 * r * s
                    c = r ** 2 + s ** 2
                    per = a + b + c
                    self.res += self.max // per
                r += 2
            s += 1

    def count_60_degrees(self):
        s = 1
        while 2*s**2 <= 3*self.max:
            r = 2*s
            while(r+s)*(2*r-s) <= 3*self.max:
                if math.gcd(r, s) == 1:
                    a = r ** 2 - r * s + s ** 2
                    b = 2 * r * s - s ** 2
                    c = r ** 2 - s ** 2
                    pgcd = math.gcd(a, math.gcd(b, c))
                    if pgcd > 1:
                        a //= pgcd
                        b //= pgcd
                        c //= pgcd
                    per = a + b + c
                    if per <= self.max:
                        self.res += self.max // per
                r += 1
            s += 1

    def count_120_degrees(self):
        s = 1
        while 2*s**2 <= self.max:
            r = 2*s
            while(r+s)*(2*r+s) <= 3*self.max:
                if math.gcd(r, s) == 1:
                    a = r ** 2 + r * s + s ** 2
                    b = 2 * r * s + s ** 2
                    c = r ** 2 - s ** 2
                    if b <= c:
                        pgcd = math.gcd(a, math.gcd(b, c))
                        if pgcd > 1:
                            a //= pgcd
                            b //= pgcd
                            c //= pgcd
                        per = a + b + c
                        if per <= self.max:
                            self.res += self.max // per
                r += 1
            s += 1

    def solve(self):
        self.count_90_degrees()
        self.count_60_degrees()
        self.count_120_degrees()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
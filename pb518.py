import time
import sys
import primes
import math


class Problem():

    def __init__(self, n):
        self.n = n
        self.primes_set = set(primes.sieve8(self.n))
        self.res = 0

    def get(self):
        for x in range(1, self.n//4):
            for y in range(1, self.n):
                a = x*y*y-1
                if a >= self.n:
                    break
                if a not in self.primes_set:
                    continue
                for z in range(y+1, self.n):
                    if math.gcd(y, z) != 1:
                        continue
                    c = x*z*z-1
                    if c >= self.n:
                        break
                    if c in self.primes_set:
                        b = x*y*z-1
                        if b in self.primes_set:
                            self.res += a+b+c

    def solve(self):
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(10**8)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

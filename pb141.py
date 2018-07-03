import time
import sys
import math


class Problem():

    def __init__(self):
        self.limit = 10**12
        self.res = 0

    @staticmethod
    def is_square(n):
        return int(math.sqrt(n))**2 == n

    def get(self):
        for x in range(1, 353554):
            for y in range(1, self.limit):
                if x**2*y**4+x*y**2 > self.limit:
                    break
                for z in range(y+1, self.limit):
                    if math.gcd(y, z) != 1:
                        continue
                    n = z**3*x**2*y + x*y**2
                    if n > self.limit:
                        break
                    if self.is_square(n):
                        self.res += n

    def solve(self):
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())


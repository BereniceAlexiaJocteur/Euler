import math
import fractions
import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n

    @staticmethod
    def issquare(x):
        rac = math.sqrt(x)
        return rac == int(rac)

    def get_count(self):
        compteur = 0
        for i1 in range(1, self.n+1):
            for i2 in range(1, self.n+1):
                g12 = fractions.gcd(i1, i2)
                for i3 in range(1, self.n+1):
                    g23 = fractions.gcd(i2, i3)
                    aplusc = i1 + i3
                    for i4 in range(1, self.n+1):
                        if self.issquare(1+(aplusc*(i2+i4)-g12-g23-fractions.gcd(i3, i4)-fractions.gcd(i4, i1))/2):
                            compteur += 1
        return compteur

    def solve(self):
        print(self.get_count())


def main():
    start = time.perf_counter()
    u = Problem(100)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
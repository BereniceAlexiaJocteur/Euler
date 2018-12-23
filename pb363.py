import math
import scipy.integrate
import time
import sys


class Problem():

    def __init__(self):
        self.v = 2 - math.sqrt((22 - 5 * math.pi) / 3)
        self.res = 0
        self.leng = 0  # longueur de la courbe de bezier

    def get_res(self):
        self.res = 100 * (self.leng - math.pi / 2) / (math.pi / 2)

    def get_length(self):
        self.leng = scipy.integrate.quad(
            lambda x: math.sqrt((9 * self.v * x ** 2 - 12 * self.v * x + 3 * self.v - 6 * x ** 2 + 6 * x) ** 2
                                + (-9 * self.v * x ** 2 + 6 * self.v * x + 6 * x ** 2 - 6 * x) ** 2), 0, 1)[0]

    def solve(self):
        self.get_length()
        self.get_res()
        print(self.res)


def main():
    start = time.time()
    u = Problem()
    u.solve()
    print('temps d execution', time.time() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

import time
import sys
import sympy
import math


class Problem():

    def __init__(self, n):
        self.n = n
        self.dict_spn = dict()
        self.res = 0

    def s_1factor(self, p, n):
        try:
            return self.dict_spn[(p, n)]
        except KeyError:
            if n > p:
                v = int(math.log(1 + n * (p - 1), p))
                a = (p**v - 1) // (p - 1)
                r = n
                sum_of_k = 0
                while r != 0:
                    k, r = divmod(r, a)
                    sum_of_k += k
                    a = (a - 1) // p
                u = (p - 1) * n + sum_of_k
                self.dict_spn[(p, n)] = u
                return u
            else:
                u = p * n
                self.dict_spn[(p, n)] = u
                return u

    def s(self, n):
        dict_factors = sympy.factorint(n)
        list_factors = list(dict_factors.items())
        list_of_s = [self.s_1factor(i, j) for (i, j) in list_factors]
        return max(list_of_s)

    def get_res(self):
        for i in range(2, self.n + 1):
            self.res += self.s(i)

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(10**8)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())

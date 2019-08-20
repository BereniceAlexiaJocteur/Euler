import time
import sys


class Problem():
    def __init__(self):
        self.period_list = [32, 26, 444, 1628, 5906, 80, 126960, 380882, 2097152]
        self.difference_list = [126, 126, 1778, 6510, 23622, 510, 507842, 1523526, 8388606]
        self.res = 0

    def get_u_2_2n1_k(self, n, k):
        t = n + 5
        period = self.period_list[n - 2]
        difference = self.difference_list[n - 2]
        q, r = divmod(k - t, period)
        period_term = self.get_period_term(n, r)
        ulam = q * difference + period_term
        return ulam

    def get_period_term(self, n, which_one):
        first_even_term = 2
        second_even_term = 4 * n + 4
        odd_terms = set([2 * i + 1 for i in range(n, 2 * n + 2)])
        d = 4 * n + 5
        count = 0
        while True:
            if (d - first_even_term in odd_terms) ^ (d - second_even_term in odd_terms):
                if count == which_one:
                    return d
                odd_terms.add(d)
                count += 1
            d += 2

    def get_res(self):
        for n in range(2, 11):
            self.res += self.get_u_2_2n1_k(n, 10**11)

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
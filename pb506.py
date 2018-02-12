import time
import sys


class Problem():

    def __init__(self):
        self.n = 10**14
        self.mod = 123454321
        self.current_element_in_cycle = ['1', '2', '3', '4', '32', '123', '43', '2123', '432', '1234', '32123', '43212',
                                         '34321', '23432', '123432']
        self.suffix = ['234321', '343212', '432123', '321234', '123432', '432123', '212343', '432123', '123432',
                       '321234', '432123', '343212', '234321', '123432', '123432']
        self.res = 0

    def get_res(self):
        q = self.n // len(self.current_element_in_cycle)
        r = self.n % len(self.current_element_in_cycle)
        cycle_q = q // 55555
        cycle_r = q % 55555
        for i in range(len(self.current_element_in_cycle)):
            self.res += int(self.current_element_in_cycle[i])
        for i in range(55554):
            for j in range(len(self.current_element_in_cycle)):
                self.current_element_in_cycle[j] = str(int(self.current_element_in_cycle[j] + self.suffix[j]) % self.mod)
                self.res = (self.res + int(self.current_element_in_cycle[j])) % self.mod
        self.res = (self.res * cycle_q) % self.mod
        for i in range(cycle_r):
            for j in range(len(self.current_element_in_cycle)):
                self.current_element_in_cycle[j] = str(int(self.current_element_in_cycle[j] + self.suffix[j]) %
                                                       self.mod)
                self.res = (self.res + int(self.current_element_in_cycle[j])) % self.mod
        for i in range(r):
            self.current_element_in_cycle[i] = str(int(self.current_element_in_cycle[i] + self.suffix[i]) % self.mod)
            self.res = (self.res + int(self.current_element_in_cycle[i])) % self.mod

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

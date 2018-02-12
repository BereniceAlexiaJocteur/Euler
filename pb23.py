# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import eulerfun


class Problem():

    def __init__(self):
        self.lim = 28123
        self.list_abundants = []
        self.sum_2abundants = set()

    def init_abundants(self):
        for i in range(1, self.lim):
            if eulerfun.d(i) > i:
                self.list_abundants.append(i)

    def init_sum_2abundants(self):
        sums = []
        for i in range(len(self.list_abundants)):
            temp1 = self.list_abundants[i]
            for j in range(i, len(self.list_abundants)):
                temp = temp1 + self.list_abundants[j]
                if temp > self.lim:
                    break
                sums.append(temp)
        self.sum_2abundants = set(sums)

    def solve(self):
        self.init_abundants()
        self.init_sum_2abundants()
        diff = set(range(self.lim)) - self.sum_2abundants
        print(sum(diff))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
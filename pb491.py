# -------------------------------------------------------------------------------
# Name:        pb491
# Purpose:     project euler
# Created:     07/09/2015
# -------------------------------------------------------------------------------

import itertools
import time
import sys


class Problem():

    def __init__(self):
        self.candidates = set()
        self.fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
        self.combi = [9, 1, 3, 6, 10, 15, 21, 28, 36, 45]

    def get_candidates(self):
        for i in itertools.combinations(list(range(10))+list(range(10)), 10):
            if sum(i) % 11 == 1:
                j = tuple(sorted(list(i)))
                self.candidates.add(j)

    def get_number_permutations(self, candi):
        result = 1
        temp = 1
        diff = len(candi) - len(set(candi))
        if candi.count(0) == 0:
            for i in range(diff):
                result *= self.combi[-1-2*i]
            result *= self.fact[10-diff*2]
            result **= 2
            return result
        elif candi.count(0) == 1:
            result *= self.combi[0]
            for i in range(diff):
                result *= self.combi[-2*(i+1)]
            result *= self.fact[9-diff*2]
            for i in range(diff):
                temp *= self.combi[-1-2*i]
            temp *= self.fact[10-diff*2]
            result *= temp
            return result
        else:
            result *= self.combi[-2]
            for i in range(diff-1):
                result *= self.combi[-3-2*i]
            result *= self.fact[10-diff*2]
            for i in range(diff):
                temp *= self.combi[-1-2*i]
            temp *= self.fact[10-diff*2]
            result *= temp
            return result

    def solve(self):
        count = 0
        self.get_candidates()
        for i in self.candidates:
            count += self.get_number_permutations(i)
        print(count)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
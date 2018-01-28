# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import itertools


class Problem():

    def __init__(self, s, n):
        self.s = s
        self.n = n - 1
        self.perm = set()

    def get_permuations(self):
        self.perm = list(set(itertools.permutations(self.s)))

    def get_nth_permutation(self):
        self.perm = sorted(self.perm)
        res = self.perm[self.n]
        temp = ''
        for i in res:
            temp += i
        return temp

    def solve(self):
        self.get_permuations()
        print(self.get_nth_permutation())


def main():
    start = time.perf_counter()
    u = Problem('0123456789', 10**6)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
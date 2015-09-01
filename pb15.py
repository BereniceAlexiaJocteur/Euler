# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import functools


class Problem():

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    @functools.lru_cache(maxsize=None)
    def get_number_paths(self, n, m):
        if n == 0 or m == 0:
            return 1
        return self.get_number_paths(n-1, m) + self.get_number_paths(n, m-1)

    def solve(self):
        print(self.get_number_paths(self.l1, self.l2))


def main():
    start = time.perf_counter()
    u = Problem(20, 20)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
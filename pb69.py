# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n):
        self.lim = n + 1
        self.phi_sieve = []

    def init_phi_sieve(self):
        visited = [False] * self.lim
        self.phi_sieve = [i for i in range(self.lim)]
        for i in range(2, self.lim):
            if not visited[i]:
                self.phi_sieve[i] = i-1
                for j in range(i + i, self.lim, i):
                    self.phi_sieve[j] = self.phi_sieve[j]//i * (i-1)
                    visited[j] = True
        del visited

    def get_max(self):
        max_ratio = 2
        ind_max = 2
        for i in range(3, self.lim):
            temp = i / self.phi_sieve[i]
            if temp > max_ratio:
                max_ratio = temp
                ind_max = i
        return ind_max

    def solve(self):
        self.init_phi_sieve()
        print(self.get_max())


def main():
    start = time.perf_counter()
    u = Problem(10**6)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
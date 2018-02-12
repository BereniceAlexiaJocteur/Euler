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
        self.collatz_list = [-1] * self.lim

    def get_collatz(self, n, tot=1):
        if n < self.lim and self.collatz_list[n] != -1:
            return tot + self.collatz_list[n] - 1
        elif n % 2 == 0:
            return self.get_collatz(n//2, tot+1)
        else:
            return self.get_collatz(3*n+1, tot+1)

    def get_max(self):
        self.collatz_list[1] = 1
        maxi = 1
        indmax = 1
        for i in range(2, self.lim):
            temp = self.get_collatz(i)
            self.collatz_list[i] = temp
            if temp > maxi:
                maxi = temp
                indmax = i
        return indmax

    def solve(self):
        print(self.get_max())


def main():
    start = time.perf_counter()
    u = Problem(10**6)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
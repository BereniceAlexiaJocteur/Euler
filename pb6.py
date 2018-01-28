# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n):
        self.lim = n

    @staticmethod
    def get_difference(n):
        temp = n*(n+1)
        sum1 = (temp//2)**2
        sum2 = temp*(2*n+1)//6
        return sum1 - sum2

    def solve(self):
        print(self.get_difference(self.lim))


def main():
    start = time.perf_counter()
    u = Problem(100)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
# -------------------------------------------------------------------------------
# Name:       pb188
# Purpose:    project eueler
# Created:    07/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def probleme(a, b, m):
    x = 1
    for i in range(2, b):
        y = pow(a, x, m)
        x = y
    return x


def main():
    startt = time.perf_counter()
    print(probleme(1777, 1855, 10**8))
    print('temps d execution', time.perf_counter() - startt, 'sec')

if __name__ == '__main__':
    sys.exit(main())
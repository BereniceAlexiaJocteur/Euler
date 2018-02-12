# -------------------------------------------------------------------------------
# Name:        pb137
# Purpose:     project euler
# Created:     22/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def a(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 15
    else:
        return 8*a(n-1)-8*a(n-2)+a(n-3)


def main():
    start = time.perf_counter()
    print(a(15))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
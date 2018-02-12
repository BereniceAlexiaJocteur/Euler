# -------------------------------------------------------------------------------
# Name:        pb169
# Purpose:     project euler
# Created:     23/07/2015
# -------------------------------------------------------------------------------

import functools
import time
import sys


@functools.lru_cache()
def a(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return a(n // 2)
    else:
        u = n // 2
        return a(u) + a(u + 1)


def main():
    start = time.perf_counter()
    print(a(10**25+1))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
# -------------------------------------------------------------------------------
# Name:        pb164
# Purpose:     project euler
# Created:     23/01/2016
# -------------------------------------------------------------------------------

import functools
import time
import sys


@functools.lru_cache(maxsize=None, typed=False)
def fonction(a, b, n):
    if n == 20:
        return 1
    if n == 0:
        return sum(fonction(b, x, n+1) for x in range(1, 10-a-b))
    return sum(fonction(b, x, n+1) for x in range(10-a-b))


def main():
    start = time.perf_counter()
    print(fonction(0, 0, 0))
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())

# -------------------------------------------------------------------------------
# Name:        pb120
# Purpose:     project euler
# Created:     16/02/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    s = 0

    for a in range(3, 1001):
        s += 2 * a * ((a - 1) // 2)

    print(s)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
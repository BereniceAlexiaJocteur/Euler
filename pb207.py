# -------------------------------------------------------------------------------
# Name:        pb207
# Purpose:     project euler
# Created:     22/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    lim = 1/12345
    i = 262144

    while (17/i) < lim:
        i -= 1

    print((i+2)*(i+1))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
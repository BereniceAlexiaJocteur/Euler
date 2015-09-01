# -------------------------------------------------------------------------------
# Name:        pb73
# Purpose:     projet eueler
# Created:     14/07/2015
# -------------------------------------------------------------------------------

import fractions
import time
import sys


def main():
    start = time.perf_counter()
    a = 3
    b = 2
    limit = 12000
    result = 0

    for d in range(5, limit+1):
        for n in range(int(d / a + 1), int((d - 1) / b + 1)):
            if fractions.gcd(n, d) == 1:
                result += 1

    print(result)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
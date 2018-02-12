# -------------------------------------------------------------------------------
# Name:        pb250
# Purpose:     project euler
# Created:     24/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    m = 250
    freq, t = [0]*m, [0]*m

    for i in range(1, 250251):
        freq[pow(i, i, m)] += 1

    t[0] = 1

    for i in range(m):
        for j in range(freq[i]):
            t = [(t[k] + t[(k-i)]) % 10**16 for k in range(m)]

    print(t[0]-1)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
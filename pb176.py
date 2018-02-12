# -------------------------------------------------------------------------------
# Name:        pb176
# Purpose:     projct euler
# Created:     04/09/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    print(2**10*3**6*5**5*7**3*11**2)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
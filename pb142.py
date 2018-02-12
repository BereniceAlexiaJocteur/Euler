# -------------------------------------------------------------------------------
# Name:        pb142
# Purpose:     project euler
# Created:     24/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    squares = set(n*n for n in range(1, 1000))

    for a in range(1, 926):
        a2 = a * a
        for b in range(1, a):
            b2 = b * b
            if (a2 - b2) in squares:
                for c in range(1, b):
                    c2 = c * c
                    if (b2 - c2) in squares and (a2 - c2) in squares and (a2+b2+c2) % 2 == 0:
                        if a2 > b2 - c2 and b2 > a2 - c2 and c2 > a2 - b2:
                            print((a2+b2+c2)//2)
                            break
                else:
                    continue
                break
        else:
            continue
        break

    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
# -------------------------------------------------------------------------------
# Name:        pb206
# Purpose:     project euler
# Created:     18/02/2015
# -------------------------------------------------------------------------------

import math
import time
import sys


def issqfree(n):
    rac = math.sqrt(n)
    return rac == int(rac)


def main():
    start = time.perf_counter()
    for a1 in range(3):
        for a2 in range(10):
            for a3 in range(10):
                for a4 in range(10):
                    for a5 in range(10):
                        for a6 in range(10):
                            for a7 in range(10):
                                for a8 in range(10):
                                    somme = 40 * a1 + 10 ** 3 * a2 + 10 ** 5 * a3 + 10 ** 7 * a4 + 10 ** 9 * a5 + \
                                        10 ** 11 * a6 + 10 ** 13 * a7 + 10 ** 15 * a8 + 10203040506070809
                                    if issqfree(somme):
                                        print(int(math.sqrt(somme) * 10))
                                        break
                                else:
                                    continue
                                break
                            else:
                                continue
                            break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
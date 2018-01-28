# -------------------------------------------------------------------------------
# Name:        pb60
# Purpose:     project euler
# Created:     14/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def test(one, two):
    if primes.is_prime_opti(int(str(one)+str(two))) and primes.is_prime(int(str(two)+str(one))):
        return True
    return False


def main():
    start = time.perf_counter()
    premiers = {}

    for i in range(2, 10000):
        premiers[i] = True

    for i in range(2, 10000):
        c = 2
        j = i * 2
        while j < 10000:
            premiers[j] = False
            c += 1
            j = i * c

    for p1 in range(2, 10000):
        if premiers[p1]:
            for p2 in range(p1, 10000):
                if premiers[p2] and test(p1, p2):
                    for p3 in range(p2, 10000):
                        if premiers[p3] and test(p1, p3) and test(p2, p3):
                            for p4 in range(p3, 10000):
                                if premiers[p4] and test(p1, p4) and test(p2, p4) and test(p3, p4):
                                    for p5 in range(p4, 10000):
                                        if premiers[p5] and test(p1, p5) and test(p2, p5) and test(p3, p5) and test(p4, p5):
                                            print(str(p1)+" "+str(p2)+" "+str(p3)+" "+str(p4)+" "+str(p5))
                                            print(p1+p2+p3+p4+p5)
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
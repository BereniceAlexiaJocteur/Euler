# -------------------------------------------------------------------------------
# Name:        pb51
# Purpose:     project euler
# Created:     15/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    p1 = primes.primes(500000)
    p2 = []

    for i in range(len(p1)):
        if str(p1[i]).count('0') == 3 or str(p1[i]).count('1') == 3 or str(p1[i]).count('2') == 3:
            p2.append(p1[i])

    for j in range(len(p2)):
        s = str(p2[j])
        if s.count('0') == 3:
            if s.rindex('0') != len(s):
                a = s.replace('0', '1')
                b = s.replace('0', '2')
                c = s.replace('0', '3')
                d = s.replace('0', '4')
                e = s.replace('0', '5')
                f = s.replace('0', '6')
                g = s.replace('0', '7')
                h = s.replace('0', '8')
                i = s.replace('0', '9')
                compt = 0
                for k in [a, b, c, d, e, f, g, h, i]:
                    if primes.is_prime_opti(int(k)):
                        compt += 1
                if compt == 7:
                    print(s)
                    break
        if s.count('1') == 3:
            if s.rindex('1') != len(s):
                b = s.replace('1', '2')
                c = s.replace('1', '3')
                d = s.replace('1', '4')
                e = s.replace('1', '5')
                f = s.replace('1', '6')
                g = s.replace('1', '7')
                h = s.replace('1', '8')
                i = s.replace('1', '9')
                compt = 0
                for k in [b, c, d, e, f, g, h, i]:
                    if primes.is_prime_opti(int(k)):
                        compt += 1
                if compt == 7:
                    print(s)
                    break
        if s.count('2') == 3:
            if s.rindex('2') != len(s):
                c = s.replace('2', '3')
                d = s.replace('2', '4')
                e = s.replace('2', '5')
                f = s.replace('2', '6')
                g = s.replace('2', '7')
                h = s.replace('2', '8')
                i = s.replace('2', '9')
                compt = 0
                for k in [c, d, e, f, g, h, i]:
                    if primes.is_prime_opti(int(k)):
                        compt += 1
                if compt == 7:
                    print(s)
                    break

    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
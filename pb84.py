# -------------------------------------------------------------------------------
# Name:        pb84
# Purpose:     project euler
# Created:     13/07/2015
# -------------------------------------------------------------------------------

import random
import numpy
import time
import sys


def f(a, n):
    return numpy.argsort(a)[::-1][:n]


def affichage(n):
    s = ''
    for j in range(len(n)):
        s += str(n[j])
    return s


def main():
    start = time.perf_counter()
    visited = [0] * 40
    position = 0
    double = 0

    for i in range(1, 1000000):
        de1 = random.randint(1, 4)
        de2 = random.randint(1, 4)
        if de1 == de2:
            double += 1
        else:
            double = 0
        if double == 3:
            position = 10
            double = 0
        else:
            position = (position + de1 + de2) % 40
            if position == 7 or position == 22 or position == 36:
                ch = random.randint(1, 16)
                if ch == 1:
                    position = 0
                elif ch == 2:
                    position = 10
                elif ch == 3:
                    position = 11
                elif ch == 4:
                    position = 24
                elif ch == 5:
                    position = 39
                elif ch == 6:
                    position = 5
                elif ch == 7 or ch == 8:
                    if position == 7:
                        position = 15
                    elif position == 22:
                        position = 25
                    else:
                        position = 5
                elif ch == 9:
                    if position == 22:
                        position = 28
                    else:
                        position = 12
                elif ch == 10:
                    position -= 3
            if position == 2 or position == 17 or position == 33:
                cc = random.randint(1, 16)
                if cc == 1:
                    position = 0
                elif cc == 2:
                    position = 10
            if position == 30:
                position = 10
        visited[position] += 1

    print(affichage(f(visited, 3)))
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
from math import *
import time


def eq(x, y):
    if x == y:
        return 1
    else:
        return 0


def c(r, s):
    if s < 0:
        return 0
    elif r == 1:
        return 1 - (s % 2)
    elif r == 2:
        return c1(2, s) + c2(2, s) + eq(s, 0)
    elif r % 2 == 1:
        return c(r, s-r+1) + c(r, s-r-1) + eq(s, 0)
    else:
        return c1(r, s) + c2(r, s) + eq(s, 0)


def c1(r, s):
    if s <= 0:
        return 0
    elif r == 2:
        return c(2, s-1)
    else:
        return c2(r, s-1) + eq(s, 1)


def c2(r, s):
    if s <= 0:
        return 0
    elif r == 2:
        return c1(2, s-2) + eq(s, 2)
    else:
        return c1(r, s-r+2) + c1(r, s-r) + eq(s, r-2) + eq(s, r)


def t(r, s):
    if r > s:
        return t(s, r)
    elif r % 2 == 1 and r > 1:
        return 2*c(r, s)
    else:
        return c(r, s)


print(t(1, 5))


start = time.perf_counter()
test = True
res = 0
i = 0
while test:
    i += 2
    compt = 0
    for j in range(1, int(sqrt(i))):
        if i % j == 0:
            if t(j, i/j) == 0:
                compt += 1
    if compt == 1:
        res = i
        test = False
print(res)
print('temps d execution', time.perf_counter() - start, 'sec')
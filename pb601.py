from math import gcd
from functools import reduce


def lcm(denominators):
    return reduce(lambda a, b: a*b // gcd(a, b), denominators)


def p(s, n):
    return (n-2)//lcm(range(1, s+1)) - (n-2)//lcm(range(1, s+2))


def solve():
    res = 0
    for i in range(1, 32):
        res += p(i, 4**i)
    return res


print(solve())

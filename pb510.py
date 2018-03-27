import math
import time


def solve(n):
    res = 0
    for a in range(1, int(n**0.5+1)):
        a2 = a * a
        for b in range(1, a+1):
            ab1 = a * b
            ab2 = a + b
            c = ab1 // ab2
            if ab1 % ab2 == 0 and math.gcd(a, math.gcd(b, c)) == 1:
                b2 = b * b
                c2 = c * c
                temp = c2 + a2 + b2
                div = n // a2
                res += (div * (div + 1) // 2) * temp
    return res


start = time.perf_counter()
print(solve(10**9))
print('temps d\'exécution', time.perf_counter() - start, 'sec')
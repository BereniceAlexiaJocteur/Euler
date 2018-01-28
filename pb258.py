# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import functools
import eulerfun
import time


start = time.perf_counter()


def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda u, v: u*v, n)

    for n_i, a_i in zip(n, a):
        pc = prod / n_i
        sum += a_i * mul_inv(pc, n_i) * pc
    return prod, int(sum % prod)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def decimal_to_base(n, b):
    t = []
    d = n
    while d > 0:
        d, r = divmod(d, b)
        t.append(r)
    return t


def lucas(n, m, q):
    res = 1
    n2 = decimal_to_base(n, q)
    m2 = decimal_to_base(m, q)
    for k in range(len(n2)):
        if k > len(m2) - 1:
            temp = 0
        else:
            temp = m2[k]
        res = (res * eulerfun.binomial(n2[k], temp)) % q
    return res


t2 = [lucas(5*10**14, i, 2) for i in range(2000)]
t5 = [lucas(5*10**14, i, 5) for i in range(2000)]
t859 = [lucas(5*10**14, i, 859) for i in range(2000)]
t2339 = [lucas(5*10**14, i, 2339) for i in range(2000)]
t20092010 = [chinese_remainder([2, 5, 859, 2339], [t2[i], t5[i], t859[i], t2339[i]])[1] for i in range(2000)]
print(t20092010)
resu = []
tempo = 0
for w in t20092010:
    tempo += w
    resu.append(tempo % 20092010)
print(resu)
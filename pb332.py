import time
import math
import itertools


start = time.perf_counter()
carres = [i**2 for i in range(51)]


def get_lattice_point(r): # return all lattice points on a sphere of radius r
    l = []
    r2 = carres[r]
    for i in range(0, r+1):
        i2 = carres[max(-i, i)]
        for j in range(-r, r+1):
            j2 = carres[max(-j, j)]
            for k in range(-r, r+1):
                k2 = carres[max(-k, k)]
                if i2 + j2 + k2 == r2:
                    l.append((i, j, k))
    return l


def cross_product(t1, t2):
    return t1[1]*t2[2]-t1[2]*t2[1], t1[2]*t2[0]-t1[0]*t2[2], t1[0]*t2[1]-t1[1]*t2[0]


def dot_product(t1, t2):
    return t1[0]*t2[0]+t1[1]*t2[1]+t1[2]*t2[2]


def norm(t1):
    return math.sqrt(t1[0] * t1[0] + t1[1] * t1[1] + t1[2] * t1[2])


def angle(a, b, c):
    n1 = cross_product(c, a)
    n2 = cross_product(b, a)
    numerator = dot_product(n1, n2)
    denominator = norm(n1) * norm(n2)
    return math.acos(numerator / denominator)


def area(r, a, b, c):
    abc = angle(a, b, c)
    bca = angle(b, c, a)
    cab = angle(c, a, b)
    e = abc + bca + cab - math.pi
    return e*r**2


def A(r):
    curr_min = 4*r**3*math.pi
    l = get_lattice_point(r)
    for i in itertools.combinations(l, 3):
        try:
            ar = area(r, i[0], i[1], i[2])
            if curr_min > ar > 1e-4:
                curr_min = ar
        except:
            pass
    return curr_min


def solve():
    res = 0
    for i in range(1, 51):
        res += A(i)
    return round(res, 6)


print(solve())
print('temps d\'exécution', time.perf_counter() - start, 'sec')
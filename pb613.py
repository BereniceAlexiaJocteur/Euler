import scipy.integrate as integrate
from numpy import arccos, pi, sqrt
import time

L = 4
H = 3


def f(x, y):
    return arccos((x ** 2 + y ** 2 - 3 * y - 4 * x) / (sqrt(x ** 2 + (3 - y) ** 2) * sqrt((x - 4) ** 2 + y ** 2)))


def g(x):
    return integrate.quad(lambda y: f(x, y), 0, H * (1 - x / L))[0]


def sol():
    return integrate.quad(lambda x: g(x), 0, L)[0] / (12 * pi)


start = time.perf_counter()
print(round(sol(), 10))
print('temps d\'exécution', time.perf_counter() - start, 'sec')


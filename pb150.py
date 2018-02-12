import math
import time


def init_triangle(n):
    tri = []
    t = 0
    for i in range((int(-1+math.sqrt(1+8*n))//2)):
        tri.append([])
        for j in range(i+1):
            t = (615949 * t + 797807) % (2**20)
            tri[i].append(t - 2**19)
    return tri


def transform_triangle(tri):
    for i in tri:
        cur = i[0]
        for j in range(1, len(i)):
            cur += i[j]
            i[j] = cur
    return tri


def find_min_sum(tri):
    curr_min = 10**6
    le = len(tri)
    for j in range(le):
        cur_somme = 0
        for k in range(le-j-1):
            cur_somme += tri[j+k][k]
            if cur_somme < curr_min:
                curr_min = cur_somme
    for i in range(1, le):
        for j in range(len(tri[i])):
            cur_somme = 0
            for k in range(min(le-i, le-j)-1):
                cur_somme += tri[i+k][j+k]-tri[i+k][j-1]
                if cur_somme < curr_min:
                    curr_min = cur_somme
    return curr_min


def solve(n):
    return find_min_sum(transform_triangle(init_triangle(n)))


start = time.perf_counter()
print(solve(500500))
print('temps d\'exécution', time.perf_counter() - start, 'sec')
import time


def number_rectangles_diagonal(m, n):
    total = 0
    for i in range(2*n+1):
        if i % 2 == 0:
            for j in range(m+1):
                x = i
                y = 2*j
                dhaut = 1
                while x+dhaut < 2*n+1:
                    dbas = 1
                    test = True
                    while x-dbas >= 0 and test:
                        if y + dbas + dhaut < 2*m+1:
                            total += 1
                        else:
                            test = False
                        dbas += 1
                    dhaut += 1
        else:
            for j in range(m):
                x = i
                y = 2*j+1
                dhaut = 1
                while x + dhaut < 2*n+1:
                    dbas = 1
                    test = True
                    while x - dbas >= 0 and test:
                        if y + dbas + dhaut < 2*m+1:
                            total += 1
                        else:
                            test = False
                        dbas += 1
                    dhaut += 1
    return total


def number_of_rectangles(m, n):
    return ((m*(m+1))//2)*((n*(n+1))//2)+number_rectangles_diagonal(m, n)


def solve(m, n):
    res = 0
    l = []
    ma = max(m, n)
    for i in range(ma + 1):
        l.append([])
        for j in range(ma + 1):
            l[i].append(0)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if l[i][j] == 0:
                cur = number_of_rectangles(i, j)
                l[i][j] = cur
                l[j][i] = cur
            res += l[i][j]
    return res


start = time.perf_counter()
print(solve(47, 43))
print('temps d execution', time.perf_counter() - start, 'sec')
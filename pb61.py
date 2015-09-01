# -------------------------------------------------------------------------------
# Name:        pb61
# Purpose:     project euler
# Created:     11/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def is_cyclic(x, y):
    return str(x)[-2:] == str(y)[:2]


def main():
    start = time.perf_counter()
    triangle = []
    square = []
    pentagonal = []
    hexagonal = []
    heptagonal = []
    octagonal = []

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            triangle.append(int(res))
        ind += 1
        res = ind * (ind + 1) / 2

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            square.append(int(res))
        ind += 1
        res = ind ** 2

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            pentagonal.append(int(res))
        ind += 1
        res = ind * (3 * ind - 1) / 2

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            hexagonal.append(int(res))
        ind += 1
        res = ind * (2 * ind - 1)

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            heptagonal.append(int(res))
        ind += 1
        res = ind * (5 * ind - 3) / 2

    ind = 1
    res = 1

    while res < 10000:
        if res > 999:
            octagonal.append(int(res))
        ind += 1
        res = ind * (3 * ind - 2)

    tableau = []

    for a in range(0, len(triangle)):
        tableau.append((3, triangle[a]))

    for a in range(0, len(square)):
        tableau.append((4, square[a]))

    for a in range(0, len(pentagonal)):
        tableau.append((5, pentagonal[a]))

    for a in range(0, len(hexagonal)):
        tableau.append((6, hexagonal[a]))

    for a in range(0, len(heptagonal)):
        tableau.append((7, heptagonal[a]))

    for a in range(0, len(octagonal)):
        tableau.append((8, octagonal[a]))

    resultat = None

    for k1, v1 in tableau:
        for k2, v2 in [(k, v) for k, v in tableau if k not in [k1] and is_cyclic(v1, v)]:
            for k3, v3 in [(k, v) for k, v in tableau if k not in [k1, k2] and is_cyclic(v2, v)]:
                for k4, v4 in [(k, v) for k, v in tableau if k not in [k1, k2, k3] and is_cyclic(v3, v)]:
                    for k5, v5 in [(k, v) for k, v in tableau if k not in [k1, k2, k3, k4] and is_cyclic(v4, v)]:
                        for k6, v6 in [(k, v) for k, v in tableau if
                                       k not in [k1, k2, k3, k4, k5] and is_cyclic(v5, v)]:
                            if is_cyclic(v6, v1):
                                resultat = v1 + v2 + v3 + v4 + v5 + v6
                                break
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
import time


def solve(n):
    set_of_repunits = {1}
    base = 2
    while 1 + base + base**2 < n:
        nombre = 1 + base + base**2
        puiss = 2
        while nombre < n:
            set_of_repunits.add(nombre)
            puiss += 1
            nombre += base**puiss
        base += 1
    somme = 0
    for i in set_of_repunits:
        somme += i
    return somme


start = time.perf_counter()
print(solve(10**12))
print('temps d execution', time.perf_counter() - start, 'sec')
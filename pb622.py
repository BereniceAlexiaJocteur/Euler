from sympy.ntheory import n_order

def a(n):
    return n_order(2, 2*n+1)

def solve(n):
    somme = 0
    for i in range(1, n):
        if a(i) == 60:
            somme += 2*i+2
    return somme

print(solve(10**8))
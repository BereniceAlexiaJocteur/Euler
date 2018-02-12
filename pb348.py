import time


def palindrome(s):
    return s == s[::-1]


def solve():
    dico = dict()
    s = 0
    for j in range(10**5):
        carre = j**2
        for i in range(10**3):
            cube = i**3
            n = str(carre+cube)
            if palindrome(n):
                if n in dico:
                    dico[n] += 1
                else:
                    dico[n] = 1
    for k in dico:
        if dico[k] == 4:
            s += int(k)
    return s


start = time.perf_counter()
print(solve())
print('temps d\'exécution', time.perf_counter() - start, 'sec')

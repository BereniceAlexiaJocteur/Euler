v = ["", "1", "2", "3", "4", "32", "123", "43", "2123", "432", "1234", "32123", "43212", "34321", "23432"]


""" l est le dernier chiffre du terme précédent """


def suite(n, l1):
    q = n//15
    r = n % 15
    p = v[r]
    sol = str(p)
    if sol.endswith("1"):
        inc = "234321"
    elif sol.endswith("4"):
        inc = "321234"
    elif sol.endswith("23"):
        inc = "432123"
    elif sol.endswith("32"):
        inc = "123432"
    elif sol.endswith("43"):
        inc = "212343"
    elif sol.endswith("12"):
        inc = "343212"
    elif sol.endswith("2") and l1 == "1":
        inc = "343212"
    elif sol.endswith("2") and l1 == "3":
        inc = "123432"
    elif sol.endswith("3") and l1 == "2":
        inc = "432123"
    elif sol.endswith("3") and l1 == "4":
        inc = "212343"
    else:
        inc = "123432"
    l2 = inc[-1:]
    for i in range(1, q+1):
        sol += inc
    return sol, l2


print(suite(19, 3))


def somme(n):
    som = 0
    last = "2"
    for i in range(1, n+1):
        temptuple = suite(i, last)
        w = temptuple[0]
        x = int(w)
        som += x
        som %= 123454321
        last = temptuple[1]
    return som

print(somme(10**14))






import fractions


def f(somme_actuelle, terme_actuel):
    if terme_actuel == 45:
        if somme_actuelle == fractions.Fraction(1, 2):
            return 1
        else:
            return 0
    else:
        temp = somme_actuelle + fractions.Fraction(1, (terme_actuel + 1)**2)
        if temp <= fractions.Fraction(1, 2):
            return f(somme_actuelle, terme_actuel + 1)+f(temp, terme_actuel + 1)
        else:
            return f(somme_actuelle, terme_actuel + 1)


print(f(fractions.Fraction(0), 1))
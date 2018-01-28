def div(n):
    cur = 1
    liste = []
    while cur < n:
        if n % cur == 0:
            liste.append(cur)
        cur += 1
    return liste


def sum_divs(n):
    return sum(div(n))


t = [0]*1000001


def fonction(n):
    s = sum_divs(n)
    if s == n:
        t[n] = 1
        longueur = 1
    else:
        temp = s
        compt = 1
        l = [temp]
        while temp != n and temp < 1000000:
            temp = sum_divs(temp)
            compt += 1
            l.append(temp)
        if temp > 1000000:
            longueur = -1
            l = l[:-1]
            for j in l:
                t[j] = -1
        else:
            longueur = len(l)
            for j in l:
                t[j] = longueur
    return longueur


maximum = 5
indice = 12496
for i in range(1, 1000001):
    if t[i] == 0:
        r = fonction(i)
        if r > maximum:
            maximum = r
            indice = i
print(indice)
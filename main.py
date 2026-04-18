def almashtir(sonlar):
    yangi_sonlar = []
    for son in sonlar:
        koef = 1
        for x in str(son):
            if x != '0':
                koef *= int(x)
        yangi_sonlar.append(koef)
    return yangi_sonlar

sonlar = [12, 34, 56, 78, 90]
print(almashtir(sonlar))

sonlar = [int(i) for i in input("n ta son kiriting: ").split()]
min_son = sonlar[0]
max_son = sonlar[0]
for son in sonlar:
    if son < min_son:
        min_son = son
    if son > max_son:
        max_son = son
ortalama = (min_son + max_son) / 2
print(ortalama)

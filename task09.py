sonlar = [int(i) for i in input("7 ta son kiriting: ").split()]
min_qiymat = sonlar[0]
for son in sonlar:
    if son < min_qiymat:
        min_qiymat = son
print(min_qiymat)


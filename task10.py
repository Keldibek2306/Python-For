sonlar = [int(i) for i in input("7 ta son kiriting: ").split()]
max_qiymat = sonlar[0]
for son in sonlar:
    if son > max_qiymat:
        max_qiymat = son
print(max_qiymat)

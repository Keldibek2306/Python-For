yoshlar = [int(i) for i in input("5 ta yosh kiriting: ").split()]
summa = 0
for yosh in yoshlar:
    summa += yosh
ortalama = summa / len(yoshlar)
print(ortalama)

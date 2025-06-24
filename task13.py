narxlar = [int(i) for i in input("5 ta narx kiriting: ").split()]
min_narx = narxlar[0]
max_narx = narxlar[0]
for narx in narxlar:
    if narx < min_narx:
        min_narx = narx
    if narx > max_narx:
        max_narx = narx
print(min_narx, max_narx)

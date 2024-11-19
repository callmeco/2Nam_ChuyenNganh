from itertools import chain, product

tups = (29, 5)
tups1 = (20, 3)

print(f"Danh sach ban dau la: \n{tups}\n{tups1}")

#duyet qua 2 Tuple
mang = []
for x in tups:
    for y in tups1:
        mang.append((x, y))
        mang.append((y, x))
print(mang)

#giong hoan vi
tam = [(a,b) for a in tups for b in tups1]
tam = tam +  [(a,b) for a in tups1 for b in tups]
# tam = [(a,b) for a in tups for b in tups1] + [(a,b) for a in tups1 for b in tups]
print(tam)

#dung chain() va product()
tamThoi = list(chain(product(tups, tups1), product(tups1, tups)))
print(tamThoi)

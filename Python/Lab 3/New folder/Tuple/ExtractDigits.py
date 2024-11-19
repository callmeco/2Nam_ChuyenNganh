from itertools import chain

#lst = "Nguyen"
#lst1 = "Nhat"
#lst2 = "Truong"
#kq = list(chain(lst, lst1, lst2))
#print(kq)

lst = [(12, 3), (2, 5), (5,1), (15,7)]
print(f"Danh sach ban dau la: {lst}" )

#cach 1: Dung map(), chain() tu thu vien itertools, ser() va loop
tam = map(lambda x: str(x), chain.from_iterable(lst))
mang = set()
for i in tam:
    for j in i:
        mang.add(j)
mang = sorted(mang)
print(f"Ket qua sau khi tach la: {mang}")

#/////////////////////////////////////////////////////////////////////////////////
#khong dung thu vien itertools
#tach tung ky tu trong Tuple
chuoi = ""
for x in lst:
    for y in x:
        chuoi += str(y)
tamThoi = list(map(int, set(chuoi)))
tamThoi = sorted(tamThoi)
print(tamThoi)

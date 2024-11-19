from itertools import chain
dicts = {
    'brand' : [1, 2, 3],
    'color' : [2, 3, 4],
    'size' : [4, 5, 6]
}
print(f"Dictionary ban dau: \n{dicts}")

#dung sort()
mang = list(sorted({x for value in dicts.values() for x in value}))
print(mang)

#dung sort(), chain()
mangMoi = list(sorted(set(chain(*dicts.values()))))
print(mangMoi)

#duyet chuoi
x = list(dicts.values())
y = []
chuoi =[]
for i in x:
    y.extend(i)
for i in y:
    if i not in chuoi:
        chuoi.append(i)
chuoi.sort()
print(chuoi)
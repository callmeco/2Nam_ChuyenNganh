tups = (1,10,3,14,35,46,7,35,9,14)

print(f"Day so ban dau: {tups}")

#Cac phan tu toi da, toi thieu K trong Tuple
print("//////////////////////////////////////////////")
print("Cac phan tu toi da, toi thieu K trong Tuple")
mang = [] #tao mot mang rong
tups = list(sorted(tups)) #sap xep tang dan
#print(tups)
#enumrate dung de sinh ra chi so index (mac dinh la so 0 va co the thay doi bang bat ky so nao)
k = int(input("Nhap gia tri cho k: "))
for index, i in enumerate(tups):
    if index < k or index >= len(tups)-k:
        mang.append(i)
mang = tuple(mang)
print(mang)
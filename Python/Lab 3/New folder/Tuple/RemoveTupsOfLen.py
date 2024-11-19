lst = [(29, 5), (20,), (3,), (29, 5, 3)]
print(f"Danh sach ban dau: {lst}")

k = int(input("Nhap vao do dai cua mang muon xoa: "))

#/////////////////////////////////////////////////////////
tam = [x for x in lst if len(x) != k]
print(f"Danh sach moi: \n{tam}")

#/////////////////////////////////////////////////////////
#dung filter()
tamThoi = list(filter(lambda y: len(y) != k, lst))
print(tamThoi)

#/////////////////////////////////////////////////////////
#dung map()
dsmoi = list(map(lambda z: z, filter(lambda x: len(x) != k, lst)))
print(dsmoi)
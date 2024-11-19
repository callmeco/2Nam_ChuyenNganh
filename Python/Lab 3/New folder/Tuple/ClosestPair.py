lists = [(1,2),(7,8),(12,15),(19,23)]
tuples = (13,14)
print(f"List ban dau: {lists}")
print(f"Tuple ban dau: {tuples}")
k=1
#dung min() va lambda
#abs(): tri tuyet doi
#kq = min(lists, key=lambda x: abs(x[k - 1] - tuples[k-1]))
#print(f"Ket qua thu duoc gan nhat voi Tuple trong List la: {kq}")


#cach 2 viet ham
def key(x):
    return abs(x[k -1] - tuples[k-1])

sapXep = sorted(lists, key=key)
print(f"Ket qua gan nhat la: {sapXep[0]}")
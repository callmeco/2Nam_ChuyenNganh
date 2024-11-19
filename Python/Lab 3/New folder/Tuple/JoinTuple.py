lists = [(1,2),(1,23),(7,8),(7,15)]
print(f"Danh sach ban dau: {lists}")

#cach 1: su dung Loop()
mang = []
for i in lists:
    if mang and mang[-1][0] == i[0]:
        mang[-1].extend(i[1:])
    else:
        mang.append([j for j in i])
mang = list(map(tuple, mang))
print(mang)

#cach 2: dung dictionary
dic = {}
for x in lists:
    dic[x[0]] = dic.get(x[0], []) + list(x[1:])
mangmoi = [(k,) + tuple(gtri) for k, gtri in dic.items()]
print(mangmoi)

#cach 3: viet ham
def join(lists, index):
    if index == len(lists) - 1:
        return lists
    elif lists[index][0] == lists[index + 1][0]:
        lists[index] += lists[index + 1][1:]
        lists.pop(index + 1)
        return join(lists, index)
    else:
        return join(lists, index + 1)
    
mangmoimoi = join(lists, 0)
print(mangmoimoi)
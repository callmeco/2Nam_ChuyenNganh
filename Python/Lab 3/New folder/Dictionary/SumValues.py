dicts = {
    'brand' : 1,
    'color' : 2,
    'size' : 4
}

#ham`
def tong(dicts):
    list =[]
    for i in dicts:
        list.append(dicts[i])
    return sum(list)
print(tong(dicts))

#////////////////////////////////////////////
#dung sum()
def tong2(dicts):
    sum = 0
    for i in dicts.value():
        sum = sum + i
    return sum
print(tong2(dicts)) 
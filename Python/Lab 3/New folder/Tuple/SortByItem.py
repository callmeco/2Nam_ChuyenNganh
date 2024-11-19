tups = [('Truong', 12), ('Nguyen',1), (2111903,20), ('Nhat', 5)]

#viet theo ham
def sapXep(tups):
    lst = len(tups)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tups[j][1] > tups[j + 1][1]):
                #hoan  vi
                tam = tups[j]
                tups[j] = tups[j + 1]
                tups[j + 1] = tam
    return tups

print(sapXep(tups))

#/////////////////////////////////////////////////////////
#dung Sort()
def sapXep2(tups):
    return (sorted(tups, key= lambda x: x[1]))
print(sapXep2(tups))
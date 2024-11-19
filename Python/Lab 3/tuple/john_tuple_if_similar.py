test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 10)]

res = []
for sub in test_list:
    if res and res[-1][0]  == sub[0]:
        res[-1].extend(sub[1:])
    else:
        res.append([ele for ele in sub])
res = list(map(tuple, res))

print(str(res))
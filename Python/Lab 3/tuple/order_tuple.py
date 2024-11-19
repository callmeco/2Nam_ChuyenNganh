test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]

print("The original list is : " + str(test_list))
ord_list = ['Geeks', 'best', 'CS', 'Gfg']

temp = dict()
for key, ele in enumerate(ord_list):
	temp.setdefault(ele, []).append(key)	
res = sorted(test_list, key = lambda ele: temp[ele[0]].pop())

print("The ordered tuple list : " + str(res))

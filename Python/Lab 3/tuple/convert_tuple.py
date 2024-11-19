test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

print("The original tuple : " + str(test_tuple))

keys = ['key', 'value', 'id']

res = [{key: val for key, val in zip(keys, sub)}
						for sub in test_tuple]

print("The converted dictionary : " + str(res))

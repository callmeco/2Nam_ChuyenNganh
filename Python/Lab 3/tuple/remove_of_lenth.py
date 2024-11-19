test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

print("The original list : " + str(test_list))
K = 1
res = list(filter(lambda x : len(x) != K, test_list))
print("Filtered list : " + str(res))

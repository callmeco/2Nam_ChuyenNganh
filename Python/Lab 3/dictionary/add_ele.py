Dict = {}
print("Tạo Dict rỗng: ")
print(Dict)

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nThêm giá trị vào Dict: ")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nThêm một giá trị khác: ")
print(Dict)

Dict[2] = 'Welcome'
print("\nCập nhật key thứ 2: ")
print(Dict)

Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nThêm một key khác: ")
print(Dict)

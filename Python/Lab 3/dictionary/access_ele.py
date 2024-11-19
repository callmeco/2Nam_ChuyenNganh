Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

print("hiển thị thông tin của key = 'name':")
print(Dict['name'])

print("hiển thị thông tin của key ở vị trí thứ nhất:")
print(Dict[1])

print("hiển thị thông tin của key = 3: ")
print(Dict.get(3))

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}

print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])



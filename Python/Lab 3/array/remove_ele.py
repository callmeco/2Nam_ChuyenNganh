import array

arr = array.array('i', [1, 2, 3, 1, 5])

print ("Mảng ban đầu: ", end ="")
for i in range (0, 5):
	print (arr[i], end =" ")

print ("\r")

print ("Kết quả khi dùng pop(2) để xoá vị trí thứ 2: ", end ="")
print (arr.pop(2))

print ("Mảng sau đó: ", end ="")
for i in range (0, 4):
	print (arr[i], end =" ")

print("\r")

arr.remove(1)
print ("Kết quả khi dùng remove(1) để xoá vị trí đầu tiên: ", end ="")
for i in range (0, 3):
	print (arr[i], end =" ")

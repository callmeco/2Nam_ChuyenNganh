import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])

print ("Mảng ban đầu: ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")

print ("\r")

print ("Dùng index(2) để tìm vị trí số 2: ", end ="")
print (arr.index(2))

print ("Dùng index(1) để tìm vị trí số 1: ", end ="")
print (arr.index(1))

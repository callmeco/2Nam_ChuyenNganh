import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])

print ("Mảng ban đầu: ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")

print ("\r")

arr[2] = 6
print("thay vị trí thứ 2 bằng 6: ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")
print()

arr[4] = 8
print("thay vị trí thứ 4 bằng 8: ", end ="")
for i in range (0, 6):
	print (arr[i], end =" ")

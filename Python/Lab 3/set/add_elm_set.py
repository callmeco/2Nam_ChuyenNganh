set1 = set()
print("Initial blank Set: ")
print(set1)

set1.add(8)
set1.add(9)
set1.add((6, 7))
print("\nSet after Addition of Three elements: ")
print(set1)

for i in range(1, 6):
	set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)

set1 = set([4, 5, (6, 7)])
set1.update([10, 11])
print("\nSet after Addition of elements using Update: ")
print(set1)
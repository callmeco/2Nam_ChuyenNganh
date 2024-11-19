Tuple1 = (5, 'Welcome', 7, 'Geeks')
print("\nTuple with Mixed Datatypes: ")
print(Tuple1)

Tuple1 = (0, 1, 2, 3)
Tuple2 = ('python', 'geek')
Tuple3 = (Tuple1, Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

Tuple1 = ('Geeks',) * 3
print("\nTuple with repetition: ")
print(Tuple1)

Tuple1 = ('Geeks')
n = 5
print("\nTuple with a loop")
for i in range(int(n)):
	Tuple1 = (Tuple1,)
	print(Tuple1)

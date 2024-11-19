#Xem kích thước dữ liệu của Tuple
import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print(Tuple1)
print(Tuple2)
print(Tuple3)

print(sys.getsizeof(Tuple1))
print(sys.getsizeof(Tuple2))
print(sys.getsizeof(Tuple3))

print(Tuple1.__sizeof__())
print(Tuple2.__sizeof__())
print(Tuple3.__sizeof__())
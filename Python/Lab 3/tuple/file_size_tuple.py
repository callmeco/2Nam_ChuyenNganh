import sys 

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple1 with getsizeof: " + str(sys.getsizeof(Tuple1)) + "bytes")

print("Size of Tuple1 wiht __sizedof__: "+str(Tuple1.__sizeof__()) + "bytes")
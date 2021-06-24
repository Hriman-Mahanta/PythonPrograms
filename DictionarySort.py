# 22.Program to sort dictionaries by values.
from operator import itemgetter
lis=[{"name":"Nandini","age":20},
     {"name":"Manjeet","age":20},
     {"name":"Nikhil","age":19}]
print("List(Sorted by age)")
print(sorted(lis,key=itemgetter("age")))
print("\r")
print("List(Sorted by age and name)")
print(sorted(lis,key=itemgetter("age","name")))
print("\r")
print("List(Sorted in descending")
print(sorted(lis,key=itemgetter('age'),reverse=True))
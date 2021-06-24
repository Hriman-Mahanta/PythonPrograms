# 55. Program to remove duplicate elements from an array.
list=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    list.append(int(input()))
s=set(list)
print(s)
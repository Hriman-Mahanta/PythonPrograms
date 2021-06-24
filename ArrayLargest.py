# 9. Program to find the largest element in an array.
A=[]
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
for i in range(0,n):
    ele=int(input())
    A.append(ele)
print("The array is: ",A)
max=A[0]
for i in range(1,n):
    if A[i]>max:
        max=A[i]
print("The maximum element is: ",max)
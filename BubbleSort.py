# 27. Program to implement a bubble sort.
def BubbleSort(A):
    for i in range(0,len(A)):
        for j in range(0,len(A)-1-i):
            if A[j+1]<A[j]:
                A[j],A[j+1]=A[j+1],A[j]

list=[]
n=int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(0,n):
    list.append(int(input()))
BubbleSort(list)
print("The sorted array is: ",list)

# 26. Program to implement binary search.
A=[1,3,5,6,8,12,15]

def Binary(i):
    beg=0
    end=9
    mid=int((beg+end)/2)
    while beg<=end and A[mid]!=i:
        if i<A[mid]:
            end=mid-1
        else:
            beg=mid+1
        mid=int((beg+end)/2)
    if A[mid]==i:
        l=mid+1
    else:
        l=-1
    return l

num=int(input("Enter the item to search: "))
loc=Binary(num)
if loc==-1:
    print("The item is not present.")
else:
    print("The item is present in the location: ",loc)


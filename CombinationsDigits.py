# 45. Program to print all combinations from 3 digits.
n=int(input("Enter a 3 digit number: "))
list=[]
while(n!=0):
    list.append(n%10)
    n//=10
for i in list:
    for j in list:
        for k in list:
            if i!=j and j!=k and i!=k:
                print(i,j,k)
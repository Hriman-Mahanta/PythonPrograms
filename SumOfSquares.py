# 7. Program to find the sum of squares.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i*i
print(sum)
# 48. Program to print the sum of a series.
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=(1/i)
print(sum)
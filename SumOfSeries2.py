# 49. Program to print the sum of a series.
x=int(input("Enter a number: "))
n=int(input("Enter number of terms: "))
sum=0
for i in range(1,n+1):
    sum+=(x^i)/i
print(sum)
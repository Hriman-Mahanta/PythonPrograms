# 46. Program to find the sum of digits of a number.
n=int(input("Enter a number: "))
sum=0
while n!=0:
    sum+=n%10
    n//=10
print("The sum of digits is: ",sum)
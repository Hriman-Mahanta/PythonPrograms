# 4. Program to check a prime number.
n=int(input("Enter a number: "))
flag=0
for i in range(2,int(n/2+1)):
    if n%i==0:
        flag=1
if flag==0:
    print("The number is prime")
else:
    print("The number is not prime")
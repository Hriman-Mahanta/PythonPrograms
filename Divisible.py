# 44. Program to print all numbers in a given range divisible by a number.
n=int(input("Enter a number: "))
a=int(input("Enter lower range: "))
b=int(input("Enter upper range: "))
for i in range(a,b+1):
    if i%n==0:
        print(i,end="  ")

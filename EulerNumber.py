# 50 .Program to find euler's number.
import math
n=int(input("Enter a number: "))
sum=1
for i in range(1,n+1):
    sum+=1/math.factorial(i)
print(sum)
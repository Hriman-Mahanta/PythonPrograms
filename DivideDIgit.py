# 32. Program to check if all digits of a number divide it.
num=int(input("Enter a number: "))
flag=0
temp=num
while temp!=0:
    d=temp%10
    if num%d!=0:
        flag=1
        break
    temp=temp//10
if flag==0:
    print("The number is divisible by all its digits.")
else:
    print("The number is not divisible by all its digits.")
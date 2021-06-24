# 12. Program to print all even numbers in a range.
a=int(input("Enter the lower bound of range: "))
b=int(input("Enter the upper bound of range: "))
print("The even numbers are: ")
for i in range(a,b+1):
    if(i%2==0):
        print(i,end="  ")
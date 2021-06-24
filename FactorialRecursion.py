# 43. Program to find factorial using recursion.
def factorial(i):
    if i<=1:
        return 1
    else:
        return i*factorial(i-1)

n=int(input("Enter a number: "))
print("The factorial is: ",factorial(n))
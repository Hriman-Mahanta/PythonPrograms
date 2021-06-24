# 28. Program to print an inverted star pattern.
for i in range(10,0,-1):
    for j in range(10-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()

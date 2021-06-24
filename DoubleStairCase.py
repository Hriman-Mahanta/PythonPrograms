# 29. Program to print a double sided staircase pattern.
for i in range(2,11,2):
    for j in range(int((10-i)/2)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(10,(int((10-i)/2))):
        print(" ",end="")
    print()
    for j in range(int((10-i)/2)):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(10,(int((10-i)/2))):
        print(" ",end="")
    print()
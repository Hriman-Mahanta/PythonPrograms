# 5. Python program to find fibonacci series.
n=int(input("Enter the number of terms: "))
f1=0
f2=1
for i in range(0,n):
    sum=f1+f2
    print(f1, end="  ")
    f1=f2
    f2=sum


# 14. Program to print even length words in a string.
s=input("Enter a sentence: ")
s=s.split()
for i in s:
    if len(i)%2==0:
        print(i)
# 15. Program to count the number of vowels in a given string.
s=input("Enter a string: ")
vowels={'a','e','i','o','u','A','E','I','O','U'}
count=0
for i in s:
    if i in vowels:
        count+=1
print("The number of vowels: ",count)
# 33. Program to check if string contains all unique characters.
s=input("Enter a string: ")
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)
if len(s)==len(s1):
    print("The string contains all unique characters")
else:
    print("The string does not contain all unique characters")
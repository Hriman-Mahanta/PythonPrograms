# 23. Program to remove duplicates from string.
s=input("Enter a string: ")
list=s.split(" ")
print(list)
s1=""
for i in list:
    if i not in s1:
        s1+=" ".join(i)
print(s1)
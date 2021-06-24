# 16. Program to count the number of matching characters in two strings.
s1=input("Enter first string: ")
s2=input("Enter second string: ")
s1_set=set(s1)
s2_set=set(s2)
s3=s1_set&s2_set
print(s3)
print("The number of matching character is: ",len(s3))
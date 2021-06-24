# 13. Program to check if a string is palindrome.
string=input("Enter a string: ")
rev = ''.join(reversed(string))
print(rev)
if string==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
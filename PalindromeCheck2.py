# 58. Program to check if a string is palindrome.
string=input("Enter string:")
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")
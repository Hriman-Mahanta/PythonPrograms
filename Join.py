# 19. Program to join a list into string.
list=[]
n=int(input("Enter the number of words: "))
print("Enter the words: ")
for i in range(0,n):
    i=input()
    list.append(i)
s=" ".join(list)
print(s)
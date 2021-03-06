# 54. Program to convert binary code to gray code.
def binary_to_gray(n):
    n = int(n, 2)
    n ^= (n >> 1)
    return bin(n)[2:]


g = input('Enter binary number: ')
b = binary_to_gray(g)
print('Gray codeword:', b)
# 53. Program to convert gray code to binary code.
def gray_to_binary(n):
    n = int(n, 2)
    mask = n
    while mask != 0:
        mask >>= 1
        n ^= mask
    return bin(n)[2:]


g = input('Enter Gray codeword: ')
b = gray_to_binary(g)
print('In binary:', b)
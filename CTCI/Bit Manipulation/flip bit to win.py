"""
you have an integer and you can flip exactly ine bit from 0 to 1
fins the max length of sequence of 1 you could create
eg. 1775: 11011101111 -> 8
"""


def flipBit(num):
    longest = 0
    current_without_flip = 0
    current_with_flip = 0
    while num:
        if num & 1:
            current_with_flip += 1
            current_without_flip += 1
        else:
            current_with_flip = current_without_flip + 1
            current_without_flip = 0
        longest = max(current_with_flip, longest)
        num >>= 1
    return longest
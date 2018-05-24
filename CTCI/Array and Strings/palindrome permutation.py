"""
check whether a string is permutation of a palindrome
"""


def isPermutationOfPalindrome(s):
    hash = {}
    countOdd = 0
    for i in s.replace(" ", ""):
        hash[i] += 1
        if hash[i] % 2 == 1:
            countOdd += 1
        else:
            countOdd -= 1
    return countOdd <= 1


# check 0 / 1 one in the bitVector
def bitImplementation(s):
    s = s.replace(" ", "")
    bitVector = 0
    for c in s:
        charBit = 1 << ord(c) # map each char to one 1 in binary bit
        if charBit & bitVector == 0:
            bitVector |= charBit
        else:
            bitVector &= ~charBit
    return bitVector == 0 | bitVector & (bitVector - 1) == 0

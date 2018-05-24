"""
Determine whether a string has all unique characters
without additional data structure
"""


# common hash table
def isUniqueChars(s):
    hash = {}
    for i in s:
        if i in hash.keys():
            return False
        hash[i] = True
    return True




# bit manipulation as flag
def isUniqueChars(s):
    check = 0
    for i in s:
        val = ord(i) - ord('a')
        if check & (1 << val) > 0:
            return False
        check |= 1 << val
    return True

print isUniqueChars("abcda")
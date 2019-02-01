"""
Given two strings, write a method to decide if one is a permutation of the other
case sensitive?
white space?
"""


# first compare length, then for hash table / sort directly

def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    hash = [0] * 128
    for i in range(len(s1)):
        hash[ord(s1[i])] += 1
        hash[ord(s2[i])] -= 1
    return not filter(lambda x: x != 0, hash)



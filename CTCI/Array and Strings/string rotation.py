"""
check whether s2 is a rotation of s1, given isSubstring function
"""


def isRotation(s1, s2):
    if s1 and len(s1) == len(s2):
        return s2 in s1 + s1
    return False
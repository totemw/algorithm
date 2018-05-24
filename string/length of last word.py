"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.
"""

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.split()[len(s.split()) - 1]) if s.split() != [] else 0


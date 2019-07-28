"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

s = "loveleetcode",
return 2
"""

# hash
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        for i, c in enumerate(s):
            if hash[c] == 1:
                return i

        return -1
"""
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.
"""

# O(n ^ 2)

class Solution1:
    def getLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]

    def longestPalindrome(self, s):
        result = ''
        for i in range(len(s)):
            # odd case:
            len1 = len(self.getLongestPalindrome(s, i, i))
            if len1 > len(result):
                result = self.getLongestPalindrome(s, i, i)
            # even case:
            len2 = len(self.getLongestPalindrome(s, i, i+1))
            if len2 > len(result):
                result = self.getLongestPalindrome(s, i, i+1)
        return result

# O (n) Manacher's Algorithm
class Solution:
    def preProcess(self, s):
        if len(s) == 0:
            return "^$"
        else:
            return "^$" + "#".join(s) + "#$"

    def longestPalindrome(self, s):
        t = self.preProcess(s)
        p = [0] * 4010 # array to record length
        center = 0
        right = 0
        for i in range(1, len(t) - 1):
            mirror_index = 2 * center - i # i' = center - (i - center)
            p[i] = min(right - i, p[mirror_index]) if right > i else 0
            # Attempt to expand p[i]
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
            # if palindrome centered at i expand right bound, adjust center
            if i + p[i] > right:
                center = i
                right = i + p[i]
            # find the maximum element in p
        maxlen = 0
        center_index = 0
        for i in range(1, len(t) - 1):
            if p[i] > maxlen:
                maxlen = p[i]
                center_index = i
        return s[(center_index - 1 - maxlen) / 2, maxlen]





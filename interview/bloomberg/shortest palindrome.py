"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
"""

# two pointers

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        N = len(s)
        i = 0
        for j in range(N - 1, -1, -1):
            if s[i] == s[j]:
                i += 1

        if i == N:
            return s

        remain = s[i : N]
        return remain[::-1] + self.shortestPalindrome(s[:i]) + s[i:]


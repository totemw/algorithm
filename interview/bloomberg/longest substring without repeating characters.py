"""
Given a string, find the length of the longest substring without repeating characters.

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr = ''
        result = 0

        for c in s:
            if c in curr:
                curr = curr[curr.index(c) + 1:]
            curr += c
            result = max(result, len(curr))
        return result
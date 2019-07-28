"""
Given a string, sort it in decreasing order based on the frequency of characters.

Input:
"tree"

Output:
"eert"
"""

# hash

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        hash = {}

        for c in s:
            if c not in hash:
                hash[c] = 1
            else:
                hash[c] += 1

        bucket = [''] * (len(s) + 1)

        for key in hash.keys():
            bucket[hash[key]] += hash[key] * key

        return ''.join(bucket[::-1])
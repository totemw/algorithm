# determine whether A contains all of the characters in B
# time: O(n) space: O(26)

import collections

class Solution:
    def compare_strings(self, str1, str2):
        letters = collections.defaultdict(int)
        for i in str1:
            letters[i] += 1
        for j in str2:
            if j not in letters:
                return False
            elif letters[j] <= 0:
                return False
            else:
                letters[j] -= 1
        return True




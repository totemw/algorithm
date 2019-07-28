"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        results = []
        if not s or not wordDict:
            return []

        self.helper(results, s, 0, wordDict, [])
        return results


    def helper(self, results, s, start, wordDict, curList):
        if self.check(s[start:], wordDict):
            if start >= len(s):
                newList = " ".join(curList)
                results.append(newList)
                return

            for i in range(start+1, len(s)+1):
                if s[start:i] in wordDict:
                    curList.append(s[start:i])
                    self.helper(results, s, i, wordDict, curList)
                    curList.pop()

    def check(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not wordDict:
            return False

        length = len(s)

        canBreak = [False for i in range(length+1)]
        canBreak[0] = True

        for i in range(1, length+1):
            for j in range(i):
                if canBreak[i]:
                    continue
                if (s[j:i] in wordDict) and canBreak[j]:
                    canBreak[i] = True

        return canBreak[length]
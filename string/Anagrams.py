 # decide whether two strings are anagrams or not

import collections



# Given an array of strings, return all groups of strings that are anagrams.
# TLE - two loops and extra n space for a new list
class Solution1:
    # Using hash map, can have high complexity when the number of strings is large
    def isAnagrams(self, s1, s2):
        return collections.Counter(s1) == collections.Counter(s2)

    # may use sorted()

    def anagrams1(self, li):
        if len(li) <= 1:
            return li
        result = []
        visited = [False] * len(li)
        for index1, s1 in enumerate(li):
            hasAnagrams = False
            for index2, s2 in enumerate(li):
                if index2 > index1 and not visited[index2] \
                        and self.isAnagrams(s1, s2):
                    result.append(s2)
                    visited[index2] = True
                    hasAnagrams = True
            if not visited[index1] and hasAnagrams:
                result.append(s1)
        return result

    def anagrams2(self, li):
        strDict = {}
        result = []
        for string in li:
            if "".join(sorted(string)) not in strDict.keys():
                strDict["".join(sorted(string))] = 1
            else:
                strDict["".join(sorted(string))] += 1
        for string in li:
            if strDict["".join(sorted(string))] > 1:
                result.append(string)
        return result

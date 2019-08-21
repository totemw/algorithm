
"""
shortest way to form string
Given two strings, A and B, determine the minimum number of cocatenations of subsequences of B
to create A. Return -1 if not possible.
Ex:
A: allan
B: lan

Answer: 3 (lan + lan +lan)
"""
"""
hashmap for source string, record char and pos
each char in target, find char and check bigger pos
if return to smaller pos, + 1
"""
import collections.defaultdict
import bisect
def shortestWay(source, target):
    char_indices = collections.defaultdict(list)
    for i, c in enumerate(source):
        char_indices[c].append(i)
    result = 0
    i = 0  # next index of source to check
    for c in target:
        if c not in char_indices:  # cannot make target if char not in source
            return -1
        j = bisect.bisect_left(char_indices[c], i)  # index in char_indices[c] that is >= i
        if j == len(char_indices[c]):  # wrap around to beginning of source
            result += 1
            j = 0
        i = char_indices[c][j] + 1  # next index in source
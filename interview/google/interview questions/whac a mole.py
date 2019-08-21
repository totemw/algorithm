"""
Given an int array holes where 1 means there is a mole,
0 means no mole.
Find out the max number of moles you can hit with a mallet of width w.

Example:

Input: holes = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0], w = 5
Output: 4
Explanation: 0(11011)01000
Follow-up:
What if you have 2 mallets?

Example:

Input: holes = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0], w = 5
Output: 6
Explanation: 0(10011)0(11001)0

dp from left to right
and right to left
and sum
"""


class Solution(object):
    def mallet(self, holes, w):
        if not (holes and w):
            return 0

        if len(holes) < w:
            return 0

        result = 0
        for i in range(w):
            result += holes[i]

        for j in range(i, len(holes)):
            curr_sum = holes[j] - holes[j - w]
            result = max(result, curr_sum)

        return result
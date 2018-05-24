"""
Given 2*n + 1 numbers, every numbers occurs twice except one, find it.
"""


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ans = A[0]
        for i in range(1, len(A)):
            ans = ans ^ A[i]
        return ans


"""
Given 3*n + 1 numbers, every numbers occurs twice except one, find it.
"""

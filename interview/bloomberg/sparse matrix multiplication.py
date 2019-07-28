"""
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

"""

# hash

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        hash = {}

        for r in range(len(B)):
            for c in range(len(B[0])):
                if c not in hash:
                    hash[c] = []
                elif B[r][c] != 0:
                    hash[c].append((c, B[r][c]))

        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

        for r in range(len(result)):
            for c in range(len(result)):
                if not hash[c]:
                    continue
                else:
                    record = hash[c]
                    for index, item in record:
                        result[r][c] += A[r][index] * item

        return result

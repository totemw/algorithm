import sys
"""
Given an integer array, find a subarray with sum closest to zero.
Return the indexes of the first number and last number.
"""

# O(n logn) get an array of sums, and then sort it
class Pair:
    def __init__(self, sum, index):
        self.sum = sum
        self.index = index

class Solotion:
    def subarraySumClosest(self, arr):
        result = []
        if not arr:
            return result
        if len(arr) == 1:
            return [0, 0]

        sums = [Pair(0, 0)]
        prev = 0
        for i in range(1, len(arr) + 1):
            sums.append(Pair(prev + arr[i - 1], i))
            prev = sums[i].sum
        sums = sorted(sums, key=lambda pair: pair.sum)
        Closest = sys.maxint
        for i in range(1, len(arr) + 1):
            if Closest > sums[i].sum - sums[i - 1].sum:
                Closest = sums[i].sum - sums[i - 1].sum
                result = []
                tmp = [sums[i].index - 1, sums[i - 1].index - 1]
                tmp.sort()
                result.append(tmp[0] + 1)
                result.append(tmp[1])
        return result
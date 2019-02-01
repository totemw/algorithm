"""
Given an array of integers,
find a contiguous subarray which has the largest sum.

Note
The subarray should contain at least one number.
"""
import sys


class Solution1:
    def maxSubArray(self, arr):
        sum = 0
        maxSum = -sys.maxint
        for i in range(0, len(arr)):
            if sum < 0:
                sum = 0
            sum += arr[i]
            maxSum = max(sum, maxSum)
        return maxSum


"""
Given an array of integers,
find two non-overlapping subarrays which have the largest sum.
Return the largest sum.
Example
For given [1, 3, -1, 2, -1, 2],
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2],
they both have the largest sum 7
"""


class Solution2:
    def maxTwoSubArrays(self, nums):
        n = len(nums)
        a = nums[:]
        aa = nums[:]
        for i in range(1, n):
            a[i] = max(nums[i], nums[i] + a[i - 1])
            aa[i] = max(a[i], aa[i - 1])
        b = nums[:]
        bb = nums[:]
        for i in range(n - 2, -1, -1):
            b[i] = max(b[i + 1] + nums[i], nums[i])
            bb[i] = max(b[i], bb[i + 1])
        mx = -sys.maxint
        for i in range(n - 1):
            mx = max(aa[i] + b[i + 1], mx)
        return mx


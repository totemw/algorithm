"""
Given an array of n integer with duplicate number, and a moving window(size k),
move the window at each iteration from the start of the array,
find the maximum number inside the window at each moving.

"""

import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = collections.deque()
        ans = []
        for i in range(len(nums)):
            dq = collections.deque()
            asn = []
            for i in range(len(nums)):
                while dq and nums[dq[-1]] <= nums[i]:
                    dq.pop()
                dq.append(i)
                if dq[0] == i - k:
                    dq.popleft()
                if i >= k - 1:
                    ans.append(nums[dq[0]])
            return ans
"""
Given an array of non-negative integers, you are initially
positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution1:
    def canJump(self, arr):
        step = arr[0]
        for i in range(1, len(arr)):
            if step > 0:
                step -= 1
                step = max(step, a[i])
            else:
                return False
        return True


"""
Your goal is to reach the last index in the minimum number of jumps.
"""


class Solution2:
    def jump(self, arr):
        result = 0
        last = 0 # maximum distance tha has been reached
        curr = 0
        for i in range(len(arr)):
            if i > last:
                last = curr
                result += 1
            curr = max(curr, i+arr[i])
        return result
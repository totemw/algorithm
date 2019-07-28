"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.

"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        result = 0
        curr = 0

        stack = []

        while curr < len(height):
            while stack and height[curr] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                distance = curr - stack[-1] - 1
                bounded = min(height[curr], height[stack[-1]]) - height[top]
                result += distance * bounded

            stack.append(curr)
            curr += 1

        return result
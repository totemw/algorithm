"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
he bricks have the same height but different width.
You want to draw a vertical line from the top to the bottom and cross the least bricks.

Input: [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]

Output: 2
"""

# hash

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        hash = {}

        for r in range(len(wall)):
            currSum = 0
            for c in range(len(wall[r]) - 1):
                currSum += wall[r][c]
                if currSum not in hash:
                    hash[currSum] = 1
                else:
                    hash[currSum] += 1

        maxCross = 0
        for key in hash.keys():
            maxCross = max(maxCross, hash[key])

        return len(wall) - maxCross

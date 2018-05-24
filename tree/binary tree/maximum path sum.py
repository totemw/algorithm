"""
Given a binary tree, find the maximum path sum.
The path may start and end at any node in the tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution1:
    def maxsum(self, root):
        if not root:
            return 0
        sum = root.val
        lmax = 0
        rmax = 0
        if root.left:
            lmax = self.maxsum(root.left)
            if lmax > 0:
                sum += lmax
        if root.right:
            rmax = self.maxsum(root.right)
            if rmax > 0:
                sum += rmax
        if sum > Solution1.max:
            Solution1.max = sum
        return max(root.val, max(root.val + lmax, root.val + rmax))

    def maxPathSum(self, root):
        Solution1.max = 100000
        if not root:
            return 0
        self.maxsum(root)
        return Solution1.max


class Solution2:
    def maxSumPath(self, root):
        maxSum, _ = self.maxPathHelper(root)
        return maxSum

    def maxPathHelper(self, root):
        if not root:
            return -100000, 0
        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxPath = max(left[0], right[0], root.val + left[1] + right[1])
        single = max(left[1] + root.val, right[1] + root.val, 0)
        return maxPath, single
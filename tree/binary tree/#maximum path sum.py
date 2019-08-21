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

def maxPathSumUtil(root, res):

        # Base Case
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

            # Find maximumsum in left and righ subtree. Also
        # find maximum root to leaf sums in left and righ
        # subtrees ans store them in ls and rs
        ls = maxPathSumUtil(root.left, res)
        rs = maxPathSumUtil(root.right, res)

        # If both left and right children exist
        if root.left is not None and root.right is not None:
            # update result if needed
            res[0] = max(res[0], ls + rs + root.data)

            # Return maximum possible value for root being
            # on one side
            return max(ls, rs, 0) + root.data

            # If any of the two children is empty, return
        # root sum for root being on one side
        if root.left is None:
            return rs + root.data
        else:
            return ls + root.data

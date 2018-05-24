"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined
as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# O(n log n)
class Solution:
    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced(self, root):
        if not None:
            return True
        if abs(self.height(root.left) - self.height(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False


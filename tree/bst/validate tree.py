"""
Given a binary tree, determine if it is a valid binary search tree (BST).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution1:
    def ValidBST(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)

    def isValidBST(self, root):
        return self.ValidBST(root, -1<<32, 1<<32)




"""
Given a binary search tree  and a new tree node,
insert the node into the tree. You should keep
the tree still be a valid binary search tree.
Do it without recursion
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def insertNode(self, root, node):
        if not root:
            return node

        curt = root
        while curt != node:
            if node.val < curt.val:
                if not curt.left:
                    curt.left = node
                curt = curt.left
            else:
                if not curt.right:
                    curt.right = node
                curt = curt.right
            return root

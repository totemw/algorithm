"""
Given a binary tree, return the zigzag level order traversal of
its nodes' values.
(ie, from left to right, then right to left for the next level
and alternate between).
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# queue - recursion
class Solution1:
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1:
                res.append([])
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].insert(0, root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    def zigzagLevelOrder(self, root):
        res = []
        self.preorder(root, 0, res)
        return res



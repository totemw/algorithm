"""
Given a binary tree, flatten it to a linked list in-place.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursion

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        head = root
        while head:
            if head.left:
                leftNode = head.left
                while leftNode.right:
                    leftNode = leftNode.right
                leftNode.right = head.right
                head.right = head.left
                head.left = None
            head = head.right


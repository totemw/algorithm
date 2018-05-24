"""
Given inorder and postorder traversal of a tree,
construct the binary tree.
You may assume that duplicates do not exist in the tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = TreeNode(postorder[len(postorder) - 1])
        index = inorder.index(root.val)
        root.left = self.buildTree(inorder[0:index], postorder[0:index])
        root.right = self.buildTree(inorder[index+1:len(inorder)], postorder[index:len(postorder) - 1])
        return root


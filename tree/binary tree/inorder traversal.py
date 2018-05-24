"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# recursion
class Solution1:
    def inorderTraversal(self, root):
        if not root:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



# iteration
class Solution2:
    def inorderTraversal(self, root):
        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop
                result.append(root.val)
                root = root.right
        return result

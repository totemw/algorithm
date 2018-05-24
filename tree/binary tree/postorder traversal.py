"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# recursion
class Solution1:
    def postorderTraversal(self, root):
        if not root:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


# iteration - reverse root-right-left
class Solution2:
    def postorderTraversal(self, root):
        result = []
        if not root:
            return []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.right)
            if node.right:
                stack.append(node.right)
        result = result[::-1]
        return result



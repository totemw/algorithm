"""
Invert a binary tree.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# recursion
class Solution1:
    def invert(self, root):
        self.helper(root)

    def helper(self, node):
        left = node.left
        right = node.right
        node.left = right
        node.right = left
        if left:
            self.helper(left)
        if right:
            self.helper(right)


class Solution2:
    def invert(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
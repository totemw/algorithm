"""
Given a binary tree, write a function to get the maximum width of the given tree.
The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes
(the leftmost and right most non-null nodes in the level,
where the null nodes between the end-nodes are also counted into the length calculation.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = [(root, 0, 0)] # node, depth, pos
        start = 0
        currLevel = 0
        result = 0

        for node, depth, pos in level:
            if node:
                level.append((node.left, depth + 1, pos * 2))
                level.append((node.right, depth + 1, pos * 2 + 1))
                if currLevel != depth:
                    currLevel = depth
                    start = pos
                result = max(result, pos - start + 1)

        return result

# DFS

class Solution2(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
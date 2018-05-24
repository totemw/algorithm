"""
Given the root and two nodes in a Binary Tree. Find the lowest
common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth
which is the ancestor of both nodes.
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pathP = self.findPath(root, p)
        pathQ = self.findPath(root, q)
        lenP = len(pathP)
        lenQ = len(pathQ)
        ans = None
        x = 0
        while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
            ans = pathP[x]
            x += 1
        return ans

    def findPath(self, root, target): # pre order
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack
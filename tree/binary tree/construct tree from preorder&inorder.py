""""
Given preorder and inorder traversal of a tree,
construct the binary tree.
You may assume that duplicates do not exist in the tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# recursion - memory limit exceed
class Solution1:
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:index + 1], inorder[0:index])
        root.right = self.buildTree(preorder[index + 1:len(preorder)], inorder[index + 1:len(inorder)])
        return root


# recursion
class Solution2:
    def buildTree(self, preorder, inorder):

        def dfs(pbegin, pend, ibegin, iend):
            if pbegin >= pend:
                return None
            if pbegin + 1 == pend:
                return TreeNode(preorder[pbegin])
            range = inorder.index(preorder[pbegin])
            range -= ibegin
            ans = TreeNode(preorder[pbegin])
            ans.left = dfs(pbegin + 1, pbegin + i + 1, ibegin, ibegin + i)
            ans.right = dfs(pbegin + i + 1, pend, ibegin + i + 1, iend)
            return ans
        return dfs(0, len(preorder), 0, len(inorder))
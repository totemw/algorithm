"""
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
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
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    def levelOrder(self, root):
        res = []
        self.preorder(root, 0, res)
        return res


# queue - iteration - BFS
class Solution2:
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        q = [root]
        while q:
            new_q = []
            result.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return result


"""
bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).
"""
# recursion
class Solution3:
    def preorder(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level + 1, res)
            self.preorder(root.right, level + 1, res)

    def levelOrderBottom(self, root):
        res = []
        self.preorder(root, 0, res)
        res.reverse()
        return res

# iteration
class Solution4:
    def levelOrderBottom(self, root):
        result = []
        if not root:
            return result
        q = [root]
        while q:
            new_q = []
            result.append([n.val for n in q])
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return list(reversed(result))

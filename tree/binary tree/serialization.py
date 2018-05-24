"""
Design an algorithm and write code to serialize
and deserialize a binary tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# postorder / preorder / bfs - determine the position of the root
class Solution:
    def serialize(self, root):
        if not root:
            return ''

        def post_order(root):
            if root:
                post_order(root.left)
                post_order(root.right)
                result[0] += str(root.val) + ','
            else:
                result[0] += '#'
        result = ['']
        post_order(root)

        return result[0][:-1]

    def deserialize(self, data):
        if not data:
            return
        nodes = data.split(',')
        def post_order(nodes):
            if nodes[-1] == '#':
                nodes.pop()
                return None
            root = TreeNode(int(nodes.pop()))
            root.right = post_order(nodes)
            root.left = post_order(nodes)
            return root
        return post_order(nodes)


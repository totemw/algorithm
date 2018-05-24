"""
Design an iterator over a binary search tree with the following rules:

- Elements are visited in ascending order (i.e. an in-order traversal)
- next() and hasNext() queries run in O(1) time in average.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# inorder traversal
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.curr = root

    def hasNext(self):
        return self.curr or len(self.stack) > 0

    def next(self):
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        nxt = self.curr
        self.curr = self.curr.right
        return nxt


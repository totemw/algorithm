"""
Given a sorted (increasing order) array with unique integer elements,
write an algorithm to create a BST with minimal height
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createMinimalBST(arr):
    return createMinimalBST(arr, 0, len(arr) - 1)


def createMinimalBST(arr, start, end):
    if end < start:
        return None
    mid = (end + start) / 2
    node = TreeNode(arr[mid])
    node.left = createMinimalBST(arr, start, mid - 1)
    node.right = createMinimalBST(arr, mid + 1, end)
    return node

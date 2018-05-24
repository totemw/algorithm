"""
find the first common ancestor of two nodes in a binary tree
Avoid storing additional nodes in a data structure
"""


# with parent ref
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self


def firstCommonAncestor(p, q):
    search1 = p
    search2 = q
    parent1 = {}
    parent2 = {}
    while search1 or search2:
        if search1:
            if search1 in parent2:
                return search1
            parent1[search1] = True
            search1 = search1.parent
        if search2:
            if search2 in parent1:
                return search2
            parent2[search1] = True
            search2 = search2.parent
    return None


# without parent ref - pre-order
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(root, node):
    result = []
    frontier = [root]
    while frontier:
        next = []
        for item in frontier:
            result.append(item)
            if item == node:
                return result
            if item.left:
                next.append(item.left)
            if item.right:
                next.append(item.right)
        frontier = next
    return result


def FirstCommonAncestor(root, p, q):
    path1 = preorder(root, p)
    path2 = preorder(root, q)
    result = None
    for i in range(min(len(path1), len(path2))):
        if path1[i] == path2[i]:
            result = path1[i]
    return result
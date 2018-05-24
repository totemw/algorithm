"""
Given a binary tree in which each node contains an integer value
Design an algorithm to count the number of paths that sums to a given value
paths need to go downwards
"""


class Node:
    def __init__(self, name, val, left = None, right = None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right


def countPathsWithSum(root, k):
    return partialPath(root, k, 0, {})


# def changeHashTable(h, key, delta):
#     newCount = delta + h[key] if key in h else 0
#     if newCount == 0:
#         del h[key]
#     else:
#         h[key] = newCount
#
#
# def partialPath(root, k, sum, h):
#     if not root:
#         return 0
#     sum += root.val
#     totalPaths = h[sum - k] if sum - k in h else 0
#     if sum == k:
#         totalPaths += 1
#     changeHashTable(h, sum, 1)
#     totalPaths += partialPath(root.left, k, sum, h) + partialPath(root.right, k, sum, h)
#     changeHashTable(h, sum, -1)
#     return totalPaths


def partialPath(root, k, sum, h):
    if not root:
        return 0
    sum += root.val
    h['total'] = 0
    if sum == k:
        h['total'] += 1
    if sum - k in h:
        h['total'] += 1
    h[sum] = 0
    print h
    result = h['total'] + partialPath(root.left, k, sum, h) + partialPath(root.right, k, sum, h)
    if sum in h:
        del h[sum]
    return result

tree = Node("A",4,Node("B",-2,Node("D",7),Node("E", 4)),
                  Node("C", 7,Node("F",-1,Node("H",-1),Node("I",2,Node("K",1))),
                              Node("G", 0,None,        Node("J", -2))))

print countPathsWithSum(tree, 2)
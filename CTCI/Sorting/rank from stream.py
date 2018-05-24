"""
Imagine you are reading in a stream of integers.
implement the data structure, which supports track(x)
and getRankOfNumber(x)
return the rank of that integer (# of values <= x in the stream)

Need data structure: keep order, insert, search - BST
for getting the rank, can do in-order traversal
using tree augmentation as well - store the size of left tree
whenever we move right, we add the size of left tree
"""


def getRank(node, x):
    if x == node.val:
        return node.leftSize()
    if x < node.val:
        return getRank(node.left, x)
    if x > node.val:
        return node.leftSzie() + 1 + getRank(node.right, x)
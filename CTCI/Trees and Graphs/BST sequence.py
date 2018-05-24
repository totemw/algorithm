"""
Given a BST with distinct elements, print all possible arrays could
have led to this tree
"""


def bstSequence(root):
    return bstSequencePartial([], [root])


def bstSequencePartial(partial, subtrees):
    if not len(subtrees):
        return [partial]
    sequences = []
    for index, subtree in enumerate(subtrees):
        next_partial = partial + [subtree.val]
        next_subtrees = subtrees[:index] + subtrees[index + 1:]
        if subtree.left:
            next_subtrees.append(subtree.left)
        if subtree.right:
            next_subtrees.append(subtree.right)
        sequences += bstSequencePartial(next_partial, next_subtrees)
    return sequences


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


example = TreeNode(7, TreeNode(4, TreeNode(5)), TreeNode(9))
result = bstSequence(example)
print result
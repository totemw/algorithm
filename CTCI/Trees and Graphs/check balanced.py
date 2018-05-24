"""
check if a BST is balanced
"""

import sys

# O(n)
def checkHeight(root):
    if not root:
        return 0

    leftHeight = checkHeight(root.left)
    if leftHeight == -sys.maxint:
        return -sys.maxint

    rightHeight = checkHeight(root.right)
    if rightHeight == -sys.maxint:
        return -sys.maxint

    if abs(leftHeight - rightHeight) > 1:
        return -sys.maxint
    else:
        return 1 + max(leftHeight, rightHeight)


def isBalanced(root):
    return checkHeight(root) != -sys.maxint

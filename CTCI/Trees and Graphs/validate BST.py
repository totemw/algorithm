"""
Implement a function to check if a binary tree is a BST
"""

# in-order
lastChecked = None
def checkBST(root):
    global lastChecked
    if not root:
        return True
    if not checkBST(root.left):
        return False
    if lastChecked and root.data <= lastChecked:
        return False
    lastChecked = root.val
    if not checkBST(root.right):
        return False
    return True


# O(n) for time, O(log n) for space
def checkBST(root):
    return checkBST(root, None, None)


def checkBST(node, min, max):
    if not node:
        return True
    if (not max and node.val > max) or (not min and node.val <= min):
        return False
    return checkBST(node.left, None, node.val) and checkBST(node.right, node.val, None)

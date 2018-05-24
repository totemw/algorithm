"""
Write an algorithm to find the next node of a given node in a BST
Assume each node has a link to its parent
"""


def inorderSucc(node):
    if not node:
        return None
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr
    else:
        curr = node
        parent = node.parent
        while parent and parent.left != curr:
            curr = parent
            parent = parent.parent
        if not parent: # max node
            return None
        else:
            return parent
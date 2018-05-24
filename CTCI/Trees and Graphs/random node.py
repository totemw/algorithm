"""
return a random node from the tree - all nodes should be equally likely to be chosen
"""

# tree augmentation with size
def selectNode(root, k):
    left_size = 0
    if root.left:
        left_size = root.left.size
    if k < left_size:
        return selectNode(k, root.left)
    elif k == left_size:
        return root.val
    else:
        return selectNode(k - left_size - 1, root.right)

"""
Given a binary tree, design an algorithm to create a linked list of all nodes
at each depth
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# pre-order traversal
def createLevelLinkedList(root, lists, level):
    if not root:
        return None
    if len(lists) < level + 1:
        lists.append(ListNode(root.val))
    else:
        lists[level].next = ListNode(root.val)
    createLevelLinkedList(root.left, lists, level + 1)
    createLevelLinkedList(root.right, lists, level + 1)


def createLevelLinkedList(root):
    lists = []
    createLevelLinkedList(root, lists, 0)
    return lists

"""
delete a node in the middle
given only access to that node
"""


def deleteNode(node):
    if not node or not node.next:
        return False
    else:
        next = node.next
        node.val = next.val
        node.next = next.next
        return True
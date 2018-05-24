"""
Implement an algorithm to delete a node in the middle of a singly linked list,
given only access to that node.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# use value of next node to be the value of current node, delete next node
class Solution:
    def deleteNode(self, node):
        if not node or not node.next:
            return
        next = node.next
        node.val = next.val
        node.next = next.next
        return


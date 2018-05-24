"""
Given a linked list and a value x, partition it such that
all nodes less than x come before nodes greater than or equal to x.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# two pointer
# time O(n); space O(1)
class Solution:
    def partition(self, head, x):
        if not head:
            return None
        leftDummy = ListNode(0)
        left = leftDummy
        rightDummy = ListNode(0)
        right = rightDummy
        node = head
        while node:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        right.next = None
        left.next = rightDummy.next
        return leftDummy.next
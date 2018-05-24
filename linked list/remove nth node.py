"""
Given a linked list, remove the nth node from the end of
list and return its head.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# two pointers
class Solution:
    def removeNthFromEnd(self, head, n):
        result = ListNode(0)
        result.next = head
        tmp = result
        for i in range(0, n):
            head = head.next
        while head != None:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return result.next
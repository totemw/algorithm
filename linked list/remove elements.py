"""
Remove all elements from a linked list of integers that have value val
Given 1->2->3->3->4->5->3, val = 3, you should return the list as 1->2->4->5+

"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        curr = dummy
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next

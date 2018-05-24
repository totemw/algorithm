"""
Given a linked list, swap every two adjacent nodes and return its head.
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# iteration
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next
            p.next.next = tmp.next
            tmp.next = p.next
            p.next = tmp
            p = p.next.next
        return dummy.next

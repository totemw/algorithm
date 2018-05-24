"""
Given a list, rotate the list to the right by k places, where k is non- negative.
Given 1->2->3->4->5 and k = 2, return 4->5->1->2->3.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# form a circle
class Solution:
    def rotateRight(self, head, k):
        if k == 0:
            return head
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        count = 0
        while p.next:
            p = p.next
            count += 1
        p.next = dummy.next
        step = count - (k % count)
        for i in range(0, step):
            p = p.next
        head = p.next
        p.next = None
        return head
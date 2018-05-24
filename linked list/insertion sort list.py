"""
Sort a linked list using insertion sort.

Example
Given 1->3->2->0->null, return 0->1->2->3->null.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution1:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        curr = head
        while curr:
            pre = dummy
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            tmp = curr.next
            curr.next = pre.next
            pre.next = curr
            curr = tmp
        return dummy.next



# imporved O(n) - O(n ^ 2)
class Solution2:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        while curr:
            if curr.next and curr.next.val < curr.val:
                pre = dummy
                while pre.next and pre.next.val < curr.next.val:
                    pre = pre.next
                tmp = pre.next
                pre.next = curr.next
                curr.next = curr.next.next
                curr.next = curr.next.next
                pre.next.next = tmp
            else:
                curr = curr.next
        return dummy.next

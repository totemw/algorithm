"""
Reverse a linked list.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution1:
    # iteration
    def reverseList(self, head):
        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head = prev
        return head

    # recursion
    def reverse(self, head):
        # case 1: empty list
        if not head:
            return head
        # case 2: only one element
        if not head.next:
            return head
        # case 3: reverse from the rest after head
        newHead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return newHead


"""
Reverse a linked list from position m to n.
"""

class Solution2:
    # head is uncertain -- dummy
    def reverseBetween(self, head, m, n):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for i in range(m - 1):
            prev = prev.next
        p = prev.next
        for i in range(n - m):
            tmp = prev.next
            prev.next = p.next
            p.next = p.next.next
            prev.next.next = tmp
        return dummy.next
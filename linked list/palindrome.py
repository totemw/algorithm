"""
Implement a function to check if a linked list is a palindrome
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# stack
class Solution1:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        stack = []
        slow = head
        fast = head.next
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast: # even numbers
            stack.append(slow.val)

        curr = slow.next
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True

# reverse inplace
class Solution2:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        rhead = self.reverse(mid)
        while rhead:
            if rhead.val != head.val:
                return False
            rhead = rhead.next
            head = head.next
        return True

    def reverse(self, head):
        dummy = ListNode(0)
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next

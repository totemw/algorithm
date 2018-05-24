"""
You have two numbers represented by a linked list, where each node contains
 a single digit. The digits are stored in reverse order, such that the 1's
 digit is at the head of the list. Write a function that adds the two
 numbers and returns the sum as a linked list.
 Given 7->1->6 + 5->9->2. That is, 617 + 295.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# O (max(|l1|, |l2|))
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        prev = ListNode(0)
        dummy = prev
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) / 10

            prev.next = ListNode(val)
            prev = prev.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next

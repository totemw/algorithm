"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

"""

# no reverse => stack

#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        stack1 = []
        stack2 = []

        head1 = l1
        head2 = l2

        while head1:
            stack1.append(head1.val)
            head1 = head1.next

        while head2:
            stack2.append(head2.val)
            head2 = head2.next

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while stack1 or stack2:
            num1 = num2 = 0
            if stack1:
                num1 = stack1.pop()
            if stack2:
                num2 = stack2.pop()
            tmp = curr.next
            curr.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) / 10
            curr.next.next = tmp

        return dummy.next
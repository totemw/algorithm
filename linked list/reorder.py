#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Given a singly linked list L: L_0→_L_1→…→_L__n-1→L_n,
reorder it to: _L_0→_L__n→L_1→_L__n-1→L_2→_L__n-2→…
You must do this in-place without altering the nodes' values.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# reverse the half of the list, then merge
class Solution:
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        # reverse
        dummy = ListNode(0)
        dummy.next = head2

        p = head2.next
        head2.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next
        # merge
        p1 = head1
        p2 = head2
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
        return head
"""
Given a linked list, determine if it has a cycle in it.
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        if not head:
            return None
        p1 = head
        p2 = head
        while True:
            if p1.next:
                p1 = p1.next.next
                p2 = p2.next
                if not p1 or not p2:
                    return False
                elif p1 == p2:
                    return True
            else:
                return False

"""
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.
"""

class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None
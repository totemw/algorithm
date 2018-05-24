"""
Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop
"""

def findBeginning(head):
    slow = head
    fast = head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    curr = head
    while curr:
        if curr == fast:
            return curr
        curr = curr.next
        fast = fast.next
"""
partiton a linked list around a value x
such that node less than x come before all nodes
greater than or equal to x
"""


def partition(head, x):
    if not head or not head.next:
        return head
    leftStart, leftEnd = None
    rightStart, rightEnd = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = None
        if curr.val < x:
            if not leftStart:
                leftStart = curr
                leftEnd = leftStart
            else:
                leftEnd.next = curr
                leftEnd = curr
        else:
            if not rightStart:
                rightStart = curr
                rightEnd = rightStart
            else:
                rightEnd.next = curr
                rightEnd = curr
        curr = tmp
    if not leftStart:
        return rightStart
    else:
        leftEnd.next = rightStart
        return leftStart

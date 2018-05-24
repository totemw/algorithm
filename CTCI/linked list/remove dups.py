"""
remove duplicates from an unsorted linked list
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def deleteDups(head):
    if not head or not head.next:
        return head
    hash = {}
    curr = head
    while curr.next:
        if curr.next.val in hash:
            curr.next = curr.next.next
        else:
            hash[curr.val] = True
            curr = curr.next
    return head


def DeleteDups(head):
    if not head or not head.next:
        return head
    curr = head
    while curr.next:
        inner = curr
        while inner.next:
            if inner.next.val == curr.val:
                inner.next = inner.next.next
            else:
                inner = inner.next
        curr = curr.next


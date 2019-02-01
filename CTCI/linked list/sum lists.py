"""
Add the two numbers and returns the sums as a linked list
stored in reversed order:
7 - 1 - 6 + 5 - 9 - 2 = 617 + 295 = 912 = 2 - 1 - 9
stored in forward order
6 - 1 - 7 + 2 - 9 - 5 = 617 + 295 = 912 = 9 - 1 - 2
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


# reversed order
def addLists(l1 ,l2):
    carry = 0
    if not l1 and not l2:
        return None
    node1 = l1
    node2 = l2
    result = None
    result_head = None
    while node1 or node2 or carry:
        value = carry
        if node1:
            value += node1.val
            node1 = node1.next
        if node2:
            value += node2.val
            node2 = node2.next
        if value:
            carry = value / 10
            value %= 10
            if result:
                result.next = ListNode(value)
                result = result.next
            else:
                result = ListNode(value)
                result_head = result
    return result_head

def reverse(l):
    prev = None
    curr = l
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    l = prev
    return prev

def Reverse(l):
    if not l or not l.next:
        return l
    else:
        newNode = Reverse(l.next)
        l.next.next = l
        l.next = None
        return newNode

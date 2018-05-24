"""
find the kth to last element of a single linked list
"""


def nthToLast(head, k):
    node1 = head
    node2 = head
    while k and node2.next:
        node2 = node2.next
        k -= 1
    if k > 0:
        return None # length < k
    else:
        while node2:
            node1 = node1.next
            node2 = node2.next
        return node1
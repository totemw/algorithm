"""
Given two single linked lists, determine if two lists intersect
Return the intersecting node
"""


def intersection(head1, head2):
    if not head1 or not head2:
        return None
    l1 = head1
    l2 = head2
    len1 = 1
    len2 = 1
    while l1.next:
        l1 = l1.next
        len1 += 1
    while l2.next:
        l2 = l2.next
        len2 += 1
    diff = abs(l1 - l2)
    if l1 != l2:
        return None # not intersected
    else:
        curr1, curr2 = head1, head2 if len1 >= len2 else head2, head1
        while diff > 0:
            curr1 = curr1.next
        while curr1:
            if curr1 != curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
    return None



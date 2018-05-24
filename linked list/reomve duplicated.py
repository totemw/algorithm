"""
Given a sorted linked list, delete all duplicates
such that each element appear only once.
Given 1->1->2->3->3, return 1->2->3
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution1:
    def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        p = head
        while p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


"""
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
Given 1->2->3->3->4->4->5, return 1->2->5
"""

# the way to handle uncertain (head) node: dummy node  -- O(2n)
class Solution2:
    def deleteDuplicates(self, head):
        if not head:
            return None
        root = ListNode(0)
        root.next = head
        node = root
        while node.next and node.next.next:
            if node.next.val == node.next.next.val:
                tmp_val = node.next.val
                while node.next and node.next.val == tmp_val:
                    node.next = node.next.next
            else:
                node = node.next

        return root.next


"""
Write a removeDuplicates() function which takes a list and deletes
any duplicate nodes from the list. The list is not sorted.
"""
# O(n ^ 2)
class Solution3:
    def deleteDuplicates(self, head):
        if not head:
            return None
        curr = head
        while curr:
            inner = curr
            while inner.next:
                if inner.next.val == curr.val:
                    inner.next = inner.next.next
                else:
                    inner = inner.next
            curr = curr.next

# hash table
    def deleteDuplicates(self, head):
        if not head:
            return None
        hash = {}
        hash[head.val] = True
        curr = head
        while curr.next:
            if hash.has_key(curr.next.val):
                curr.next = curr.next.next
            else:
                hash[curr.next.val] = True
                curr = curr.next
        return head


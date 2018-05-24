"""
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.
Return a deep copy of the list.
"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

# deep copy -- maintain a hash table
class Solution1:
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        curr = dummy
        hash = {}

        while head:
            newNode = RandomListNode(head.label)
            curr.next = newNode
            hash[head] = newNode
            newNode.random = head.random
            head = head.next
            curr = curr.next

        curr = dummy.next
        while curr:
            if curr.random:
                curr.radnom = hash[curr.random]
            curr = curr.next

        return dummy.next


# create repeatitive list
class Solution2:
    def copyRandomList(self, head):
        if not head:
            return None
        curr = head
    # generate new list with node
        while curr:
            newNode = RandomListNode(curr.label)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
    # copy random pointer
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
    # split original list
        newHead = head.next
        curr = head
        while curr:
            newNode = curr.next
            curr = curr.next.next
            if newNode.next:
                newNode.next = newNode.next.next
            curr = curr.next
        return newHead

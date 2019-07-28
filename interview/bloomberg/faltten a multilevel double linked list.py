"""
You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Input:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

Output:
1-2-3-7-8-11-12-9-10-4-5-6-NULL

"""


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


# stack  BFS

class Solution(object):
    def flatten(self, head):
        if not head:
            return

        dummy = Node(0, None, head, None)
        stack = []
        stack.append(head)
        curr = dummy

        while stack:
            node = stack.pop()

            node.prev = curr
            curr.next = node

            if node.next:
                stack.append(node.next)
                node.next = None
            if node.child:
                stack.append(node.child)
                node.child = None
            curr = curr.next

        dummy.next.prev = None
        return dummy.next



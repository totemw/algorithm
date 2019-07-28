# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        h = {}

        curr = head
        newHead = RandomListNode(0)
        currNew = newHead

        while curr:
            newNode = RandomListNode(curr.label)
            currNew.next = newNode
            h[curr] = newNode
            newNode.random = curr.random
            currNew = currNew.next
            curr = curr.next

        currNew = newHead.next

        while currNew:
            if currNew.random:
                currNew.random = h[currNew.random]
            currNew = currNew.next

        return newHead.next

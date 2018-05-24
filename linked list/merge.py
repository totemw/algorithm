"""
Merge two sorted (ascending) linked lists and return it as
a new sorted list. The new sorted list should be made by
splicing together the nodes of the two lists and sorted
in ascending order.
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next


"""
Merge k sorted linked lists
"""

# divide and conquer  - sacrifice space complexity
class Solution2:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists)//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # merge left and right
        dummy = ListNode(0)
        curr = dummy
        while left or right:
            if not right or (left and left.val <= right.val):
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        return dummy.next

# min heap - priority queue
from heapq import *
class Solution3:
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0)
        curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next:
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
            heapq.heapify(heap)
        return head.next



    # implementation
    def mergeKLists(self, lists):
        self.heap = [[i, lists[i].val] for i in range(len(lists)) if lists[i]]
        self.hszie = len(self.heap)
        for i in range(self.hszie - 1, -1, -1):
            self.adjustdown(i)
        dummy = ListNode(0)
        head = dummy
        while self.hszie > 0:
            index = self.heap[0][0]
            value = self.heap[0][1]
            head.next = lists[index]
            head = head.next
            lists[index] = lists[index].next
            if not lists[index]:
                self.heap[0] = self.heap[self.hszie - 1]
                self.hszie -= 1
            else:
                self.heap[0] = [index, lists[index] - 1]
            self.adjustdown(0)
            return dummy.head

    def adjustdown(self, i):
        leftchild = lambda x : 2 * x + 1
        rightchild = lambda x : 2 * x + 2
        while True:
            min = i
            value = self.heap[i][1]
            if leftchild(i) < self.hszie and self.heap[leftchild(i)][1] < value:
                min = leftchild(i)
                value = self.heap[leftchild(i)][1]
            if rightchild(i) < self.hszie and self.heap[rightchild(i)][1] < value:
                min = rightchild(i)
                value = self.heap[rightchild(i)][1]
            if min == i:
                break
            else:
                self.heap[i], self.heap[min] = self.heap[min], self.heap[i]
                i = min
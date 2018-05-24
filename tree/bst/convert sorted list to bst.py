"""
Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def sortedArrayToBst(self, arr):
        length = len(arr)
        if length == 0:
            return None
        if length == 1:
            return TreeNode(arr[0])
        root = TreeNode[arr[length/2]]
        root.left = self.sortedArrayToBst(arr[:length/2])
        root.right = self.sortedArrayToBst(arr[length/2 + 1:])
        return root

    def sortedListToBST(self, head):
        array = []
        p = head
        while p:
            array.append(p.val)
            p = p.next
        return self.sortedArrayToBst(array)
"""
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree.
Find all the keys of tree in range k1 to k2. i.e. print all x such that k1<=x<=k2
and x is a key of given BST. Return all the keys in ascending order.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#can also use in order traversal to get a ordered list

class Solution:
    def searchRange(self, root, k1, k2):
        result = []
        if not root:
            return result
        queue = [root]
        index = 0
        while index < len(queue):
            if not queue[index]:
                if queue[index].val >= k1 and queue[index].val <= k2:
                    result.append(queue[index].val)
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1
        return sorted(result)


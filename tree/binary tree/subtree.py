"""
You have two every large binary trees: T1,
with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1.
"""

class Solution:
    def get(self, root, rt):
        if not root:
            rt.append("#")
            return
        rt.append(str(root.val))
        self.get(root.left, rt)
        self.get(root.right, rt)

    def isSubtree(self, root1, root2):
        rt = []
        self.get(root1, rt)
        t1 = ','.join(rt)
        rt = []
        self.get(root2, rt)
        t2 = ','.join(rt)
        return t1.find(t2) != -1
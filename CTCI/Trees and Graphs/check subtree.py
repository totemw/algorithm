"""
Determine whether T2 is a subtree for T1
that is, cut off T1 at node n, two trees will be identical
"""


# pre-order traversal with None representation is Unique - O(n + m) O(n + m)
def getOrderString(root):
    if not root:
        return ['X']
    return [root.val] + getOrderString(root.left) + getOrderString(root.right)


def containsTree(T1, T2):
    str1 = getOrderString(T1)
    str2 = getOrderString(T2)
    return str2 in str1


# match subtree of T1 with T2 - O(n + km) O(log n + log m)
def subTree(T1, T2):
    if not T1 and not T2:
        return False
    elif T1.val == T2.val and match(T1, T2):
        return True
    else:
        return subTree(T1.left, T2) or subTree(T1.right, T2)


def match(r1, r2):
    if not r1 and not r2:
        return True
    elif not r1 or not r2:
        return False
    elif r1.val == r2.val:
        return match(r1.left, r2.left) and match(r1.right) and match(r2.right)
    else:
        return False

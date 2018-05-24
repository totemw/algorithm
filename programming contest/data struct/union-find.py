"""
used to store disjoint sets
FInd(x): returns the "representative" of the set that x belongs
Union(x, y): merge two sets that contain x and y

Implementation:
represent each set by a rooted tree
- every node maintains a link to its parent
- root points itself
- root node is the "representative" of the set

find: follows the link from x to the rooted node
union: use find(x) and find(y) to find corresponding root nodes
and direct one to other
"""


def Find(x):
    L = []
    while x != L[x]:
        x = L[x]
    return L[x]


def Union(x, y):
    L = []
    L[Find(x)] = Find(y)


# path compresiion - makes tree shallower each time
def Find(x):
    if x == L[x]:
        return x
    root = Find(L[x])
    L[x] = root
    return root
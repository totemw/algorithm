"""
Fenwick Tree: A variant of segment trees
- Set(k, x): sets the value of kth item equal to x
- Sum(k): computes the sum of items 1 ... k, (prefix sum)
--- both can be done in O(log n) time and O(n) space

Implementation:
- Full binary tree with at least n leaf nodes
- kth leaf node stores then value of item k
- Each internal node stores the sum of values of its children
- use array

sum: p initially points  at leaf k
- if p is pointing to a left child of some nodes:
    add the value of P
    set P to the left neighbor's parent node
    if p doesn't have left neighbor, termiante
-else:
    set p to the parent node of p

"""

# -*- coding: utf-8 -*-
"""
Input: a rooted tree and a bunch of node pairs
Output: lowest common ancestors of the given pairs of nodes

Preprocessing the tree in O(n log n) time in order to answer
each LCA query in O(log n) time

Each node stores its depth, as well as the links to every 2^k th ancestor
– O(log n) additional storage per node
– We will use Anc[x][k] to denote the 2
k
th ancestor of node x
◮ Computing Anc[x][k]:
– Anc[x][0] = x’s parent
– Anc[x][k] = Anc[ Anc[x][k-1] ][ k-1 ]

◮ Given two node indices x and y
– Without loss of generality, assume depth(x) ≤ depth(y)
◮ Maintain two pointers p and q, initially pointing at x and y
◮ If depth(p) < depth(q), bring q to the same depth as p
– using Anc that we computed before
◮ Now we will assume that depth(p) = depth(q)


If p and q are the same, return p
◮ Otherwise, initialize k as ⌈log2 n⌉ and repeat:
– If k is 0, return p’s parent node
– If Anc[p][k] is undefined, or if Anc[p][k] and Anc[q][k]
point to the same node:
◮ Decrease k by 1
– Otherwise:
◮ Set p = Anc[p][k] and q = Anc[q][k] to bring p and q up
by 2
k
levels

"""
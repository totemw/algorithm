"""
Given a weighted graph with n nodes, find the shortest path
that visits every node exactly once

np-hard
brute force (n!)
dp (n^2 * 2 ^ n)

Subprobelm:
Ds,v: optimal path, visits set s, ends at v
#: n2^n

base case: D{v},v = 0

Recurrence:
Ds,v = min { Ds-{v}, u + cost(u, v)} where u belongs to S-{v}

For subsets, binary representation
bitmasks
Union: x | y
Intersection: x & y
Symmetric Difference: x ^ y
Singleton set {i}: 1 << i
Membership test: x & ((1 << i) - 1) != 0

"""
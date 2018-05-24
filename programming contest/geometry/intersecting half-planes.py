"""
Intersecting Half-planes

representing a half-plane: ax + by + c <= 0
The intersection of half-planes is a convex area

Given n half-planes, how do we compute the intersection of them?

There is an easy O(n ^ 3) and a head O(n log n)

1. For each half-plane aix + biy + ci <= 0, define a straight line
    ei: aix + biy + ci = 0
2. For each pair of ei and ej:
    - Compute their intersection p = (px, py)
    - Check if akpx + bkpy + ck <= 0 for all half-planes
        If so, store p in some array P
3. Find the convex hull of the points in P

"""
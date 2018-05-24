# coding=utf-8
"""
Given n points on the plane, find the smallest convex ploygon that contains
all the given points

Simple Algorithm
AB is an edge of the convex hull iff ccw(A, B, C) have the
same sign for all other points C.

Graham Scan
- we know that the leftmost point should be in the convex hull
- make the leftmost point the origin
- sort the points in increasing order of y/x (numbered the points)
- Incrementally construct the convex hull using the stack

that is, maintain a convex chain, it it appears a concave corner, change points

Code:
◮ Set the leftmost point as (0, 0), and sort the rest of the points
  in increasing order of y/x
◮ Initialize stack S
◮ For i = 1, . . . , n:
    – Let A be the second topmost element of S, B be the topmost
    element of S, and C be the ith point
    – If ccw(A, B, C) < 0, pop S and go back
    – Push C to S
◮ Points in S form the convex hull


"""
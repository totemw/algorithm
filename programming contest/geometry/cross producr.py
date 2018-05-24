"""
ccw(A, B, C) = (B - A) * (C - A) = (bx - ax)(cy - ay) - (by - ay)(cx - ax)


Segment - Segment Intersection Test
(intersect properly: meet point is strictly inside both segments)
condition:
- ccw(A, B, C) * ccw(A, B, D) < 0
- and ccw(C, D, A) * ccw(C, D, B) < 0
- if all of them are zero : collinear

"""
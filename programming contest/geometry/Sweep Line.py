"""
Sweep Line Algorithm

Main idea:
maintain a line (with some auxiliary data structure) that sweeps
through the entire plane and solve th problem locally

Problem:
Given n axis-aligned rectangles, find the area of the union of them
(sweep the plane from left to right)

Implementation:
If the sweep line hits the left edge of a rectangle
 - insert it to the data structure
 - remove it when hits its right edge
Move to next event, and add the area of existing area
 - O(n) for finding the union of rec's width


"""
"""
Given a tree, color nodes black as many as possible
without coloring two adjacent nodes

Sub problem: subtree

Recurrence: For node v,
v is colored: children must not be colored
Bv = 1 + sum(Wu) (u belongs to children)

v is not colored, children can have any color
Wv = sum(max{ Bu, Wu }) (u belongs to children)

base case: leaf nodes
result: max{Br, Wr}
"""
# coding=utf-8
"""
Want to find a subset of Edges with the minimum total weight
that connects all the nodes into a tree

Algorithms:
- Kruskal's algorithm
- Prim's algorithm


Kruskal's algorithm  O(m log m)
- The edge with the smallest weight has to be in the MST
- After an edge is chosen, the two nodes at the ends can be
   merged and considered as a single node

1. Sort the edges in increasing order of weight
2. Repeat until there is one supernode left:
    ◮ Take the minimum weight edge e⋆
    ◮ If e⋆ connects two different supernodes, then connect them
      and merge the supernodes (use union-find)
3.– Otherwise, ignore e⋆ and try the next edge


Prim's algorithm - depends on implementation: O(m log n) / O(m + n log n) / O(n * n + m)
- Maintain a set S that starts out with a single node s
- Find the smallest weighted edge that connects u ∈ S and v !∈ S
- Add this edge to MST, add v to S
- Repeat until S = V

1. Initialize S := {s}, Dv := cost(s, v) for every v
   – If there is no edge between s and v, cost(s, v) = ∞
2. Repeat until S = V :
   - Find v /∈ S with smallest Dv
      ◮ Use a priority queue or a simple linear search
   – Add v to S, add Dv to the total weight of the MST
   – For each edge (v, w):
      ◮ Update Dw := min(Dw, cost(v, w))


"""
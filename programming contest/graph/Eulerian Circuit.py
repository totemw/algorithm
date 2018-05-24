"""
Given an undirected graph G
Want to find a sequence of nodes that visits every edge
exactly once and comes back to the starting point

Eulerian circuits exist iff
- G is connected
- and each node has an even degree

Procedure:
Glue cycles together to finish

Related Problems:
Eulerian Path: exist iff the graph is connected and the
number of nodes with odd degree is 0 or 2

Hamiltonian Path: a Path that visits every node in
the graph exactly once
"""
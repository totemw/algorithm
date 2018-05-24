"""
Given a directed graph, where each edge e is associated with its
its capacity c(e) > 0, Teo special nodes s, t are given

Maximize the total amount of flow from s to t
 - Flow on edge e doesn't exceed c(e)
 - Fro every node v != s,t, incoming floe is equal to outgoing flow


Alternate Formulation: minimum cut

We want to remove some edges from the graph such that after removing
the edges, there is no path from s to t
The cost of removing e is equal to its capacity c(e)
Find a cut with minimum total cost

Theorem: Maximum flow = Minimum cut


Flow Decomposition
Any valid flow can be decomposed into flow paths and circulations
"""
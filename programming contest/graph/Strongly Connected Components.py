# coding=utf-8
"""
strongly connected: all nodes are reachable from every single node in V
SCC of graph are maximal strongly connected sub-graphs

Kosaraju's Algorithm O(n + m)

1. Initialize counter c := 0
2. While not all nodes are labeled:
    – Choose an arbitrary unlabeled node v
    – Start DFS from v
        ◮ Check the current node x as visited
        ◮ Recurse on all unvisited neighbors
        ◮ After the DFS calls are finished, increment c
         and set the label of x as c
4. Reverse the direction of all the edges
5. For node v with label n, n − 1, . . . , 1:
    – Find all reachable nodes from v and group them as an SCC



"""
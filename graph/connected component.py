"""
Find the number connected component in the undirected graph.
Each node in the graph contains a label and a list of its neighbors.
(a connected component (or just component) of an undirected graph is a
subgraph in which any two vertices are connected to each other by paths,
and which is connected to no additional vertices in the supergraph.)
"""

# dfs
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)

    def connectedSet(self, nodes):
        self.v = {}
        for node in nodes:
            self.v[node.label] = False

        result = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                result.sppend(sorted(tmp))
        return result
"""
Given a directed graph, design an algorithm to find out
whether there is a route between two nodes.
"""

class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def dfs(self, i, check, graph, t):
        if check[i] == 1:
            return False
        if i == t:
            return True
        check[i] = 1
        for j in i.neighbors:
            if check[j] == 0 and self.dfs(j, check, graph, t):
                return True
        return False

    def routeBetweenTwoNodesInGraph(self, graph, s, t):
        check = {}
        for x in graph:
            check[x] = 0
        return self.dfs(s, check, graph, t)

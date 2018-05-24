"""
Given an directed graph, a topological order of the graph nodes is defined as follow:

For each directed edge A -> B in graph, A must before B in the order list.
The first node in the order can be any node in the graph with no nodes direct to it.
Find any topological order for the given graph.
"""


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def dfs(self, i, level, ans):
        ans.append(i)
        level[i] -= 1
        for j in i.neighbors:
            level[j] = level[j] - 1
            if level[j] == 0:
                self.dfs(j, level, ans)

    def topSort(self, graph):
        level = {}
        for x in graph:
            level[x] = 0

        for i in graph:
            for j in i.neighbors:
                level[j] = level[j] + 1

        ans = []
        for i in graph:
            if level[i] == 0:
                self.dfs(i, level, ans)
        return ans

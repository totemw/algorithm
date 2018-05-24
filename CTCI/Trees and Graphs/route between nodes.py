"""
Given a directed graph, design an algorithm to find out whether there is a route
between two nodes
"""


class GraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


def search(start, end):
    parents = {}
    frontier = [start]
    while frontier:
        next = []
        for x in frontier:
            for n in x.neighbors:
                if n not in parents:
                    parents[n] = x
                    if n == end:
                        path = []
                        while parents[n] != start:
                            path.append(parents[n])
                            n = parents[n]
                        return [start] + path.reverse()
                    else:
                        next.append(n)
        frontier = next
    return False
"""
list of projects
list of dependencies: a list of pairs of projects
topological sort
"""


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.indegree = 0

    def addEdge(self, node):
        self.edges.append(node)
        self.indegree += 1


def BFS(node, arr):
    arr.append(node.val)
    for n in node.edges:
        n.indegree -= 1
        if not n.indegree:
            BFS(n, arr)


def buildOrder(projects, dependecies):
    graph = {}
    for project in projects:
        graph[project] = GraphNode(projects)
    for pair in dependecies:
        graph[pair[0]].addEdgs(graph[pair[1]])
    result = []
    for node in projects:
        if not graph[node].indegree:
            BFS(graph[node], result)
    if len(result) < len(projects):
        raise Exception('Cycle detected')
    return result

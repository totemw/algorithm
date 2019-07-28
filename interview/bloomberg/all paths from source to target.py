"""
Given a directed, acyclic graph of N nodes.
Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.
 graph[i] is a list of all nodes j for which the edge (i, j) exists.

"""

# recursion O(2^n * n^2)

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        N = len(graph)

        def solve(node):
            if node == N - 1:
                return [[N - 1]]

            result = []

            for neighbor in graph[node]:
                for path in solve(neighbor):
                    result.append([node] + path)
            return result
        return solve(0)





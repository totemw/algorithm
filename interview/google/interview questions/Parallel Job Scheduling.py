"""
There are N processes with some processes having dependencies on other processes
(meaning if a process P1 is dependent on process P2,
then P1 can only be started after P2 is complete).
Assume that there won't be a cyclic dependency in the inputs.

Each process has a time duration (in sec) given by Duration array.

Processes can be run in parallel. We need to find the minimum time such that all processes are completed.

TestCase:
There are 4 processes -
A (Duration: 2 sec), B (Duration: 3 sec), C (Duration: 4 sec) and D (Duration: 5 sec)

B is dependent on A
C is dependent on A
D is dependent on B & C

In this case, min time would be 11 sec.

Longest Path in a Directed Acyclic Graph:
Perform the topo sort using usual algorithm.
After that pop each element one by one from stack and calculate time required for the subgraph of this node.
It will be maxTime(all nodes which have an outgoing edge from the current node) + currentNodeTime.
Calculate the max.
"""
class Solution:
    visited = {}  # ini all white
    stack =[]
    def dfs(self, v , neighbor):
        self.visited[v] = "grey"
        for n in neighbor[v]: # white
            if n not in self.visited:
                self.dfs(n, neighbor)
        self.visited[v] = "black"
        self.stack.append(v)
    dp = {}
    def findMax(self, v, neighbor):
        if v in self.dp:
            return self.dp[v]
        m = 0
        for n in neighbor[v]:
            m = max(m, self.findMax(n, neighbor))
        self.dp[v] = v.val + m
        return self.dp[v]
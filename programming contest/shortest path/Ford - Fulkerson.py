"""
Ford-Fulkerson Algorithm  - simple and practical max-flow problem

Main idea: find valid flow paths until there is none left, add them up


Code:
1. Set f total = 0
2. Repeat until there is no path from s to t:
    - Run DFS from s to find a flow path to t
    - Let f be the minimum capacaity value on the path
    - Add f to f total
    - For each edge u -> v on the path:
        - Decrease c(u -> v) by f
        - Increase c(v -> u) by f

Analysis:
- FInd flow path O(n + m)
- time complexity O((n + m) * f)
- We send at least 1 flow through the path


Find Minimum Cut:
1. First get the residual graph - operated from the original graph
2. Make all nodes reachable from s
3. seperate those nodes from others - min-cut

"""
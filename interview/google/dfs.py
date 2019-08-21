"""
template
"""
# dfs on graph

def DFS(V, Adj):
    parent = {}
    for s in V:
        if s not in parent:
            parent[s] = None
            DFS(V, Adj, s)


"""
dfs on matrix
O(mn)
"""

"""
dijkstra on graph

def dijkstra(s, d):
    pq = [(0, s)]
    while pq:
        weight, s = heapq.heappop(pq)
        if visited[s]:
            continue  # cut
        visited[s] = True
        s == d:
            return
        for all neighbors of s:
            heapq.heappush(pq, (nei's distance to start, nei))
"""

"""
dijkstra on matrix
O(mn*log(mn)) 

min heap
pop the min distance
for all possible positions
push position which meet condition
"""
import heapq

def shortestDistance(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: int
    """
    pq = [(0, start[0], start[1])]
    m = len(maze)
    n = len(maze[0])
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while pq:
        count, i, j = heapq.heappop(pq)
        if maze[i][j] == -1:
            continue  # cut
        maze[i][j] = -1  # record
        if i == destination[0] and j == destination[1]:
            return count
        for x, y in dir:
            row = i + x
            col = j + y
            local = 1
            # record local variable
            while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                row += x
                col += y
                local += 1
            row -= x
            col -= y
            local -= 1
            # print pq
            heapq.heappush(pq, (count + local, row, col))
    return -1

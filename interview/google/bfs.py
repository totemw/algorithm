"""
graph template
"""
def BFS(s):
    level = {s: 0} # record level and visited
    # parent = {s: None}
    i = 1
    queue = [s]
    while queue:
        next = []
        for v in queue:
            for nei in v.neighbors:
                if nei not in level:
                    level[nei] = i
                    # parent[nei] = v
                    next.append(v)
        queue = next
        i += 1

"""
matrix template

each level will be all possible neighbors' positions
"""
v = {} # visited
def bfs(s):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = [s]
    while queue:
        for v in queue:
            for d in direction:
                new_x = v.x + d[0]
                new_y = v.y + d[1]
                # if some condition and not visited:
                    # queue.append((new_x, new_y))


"""
the maze 490

queue
find all possible positions
if position meet reuqirement and not visited
append into queue
while loop until qmpty queue
"""


def hasPath(self, maze, start, destination):
    """
    :type maze: List[List[int]]
    :type start: List[int]
    :type destination: List[int]
    :rtype: bool
    """
    queue = [start]
    m = len(maze)
    n = len(maze[0])
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        i, j = queue.pop(0)
        # record
        maze[i][j] = -1
        if i == destination[0] and j == destination[1]:
            return True
        for x, y in dir:
            row = x + i
            col = y + j
            # move until the wall
            while 0 <= row < m and 0 <= col < n and maze[row][col] != 1:
                row += x
                col += y
            # move back a step
            row -= x
            col -= y
            if maze[row][col] == 0 and [row, col] not in queue:
                queue.append([row, col])
    return False





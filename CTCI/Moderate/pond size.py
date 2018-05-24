"""
you have an integer matrix representing a plot of land,
where the value represents the height above sea level
A value of zero indicates water (compose pond, vertically horizontally diagonally)
compute the sizes of all ponds
eg. 0 2 1 0
    0 1 0 1
    1 1 0 1
    0 1 0 1
"""


def computePondSize(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    result = []
    for r in range(len(land)):
        for c in range(len(land[r])):
            size = computeSize(land,visited, r, c)
            if size > 0:
                result.append(size)
    return result


def computeSize(land, visited, r, c):
    if r < 0 or c < 0 or r > len(land) or c > len(land[r]) \
            or visited[r][c] or land[r][c] != 0:
        size = 1
        visited[r][c] = True
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                size += computeSize(land, visited, r + dr, c + dc)
        return size

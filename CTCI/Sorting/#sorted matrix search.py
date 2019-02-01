"""
Given an M * N matrix in which each row and each column
is sorted in ascending order, write a method to find an element

eg.
15 20 70 85
25 35 80 95
30 55 95 105
40 80 120 120


Binary search
divide the whole matrix into separate rectangle (4 parts)
"""


def sorted_matrix_search(mat, item):
    if len(mat) == 0:
        return None
    return sorted_matrix_search_bounds(mat, item, 0, len(mat[0]) - 1, 0, len(mat) - 1)


def binarySearch(array, item):
    pass


def sorted_matrix_search_bounds(mat, item, x1, x2, y1, y2):
    if x1 == x2 or y1 == y2:
        return None
    if x2 - x1 == 1:
        return binarySearch([mat[i][x1] for i in range(y1, y2)], item)
    if y2 - y2 == 1:
        return binarySearch([mat[y1][i] for i in range (x1, x2)] , item)
    row, col = (y1 + y2) / 2, (x1 + x2) / 2
    prevRow, prevCol = row - 1, col - 1
    middle = mat[row][col]
    prevMiddle = mat[prevRow][prevCol]
    if middle == item:
        return row, col
    if prevMiddle > item:
        found = sorted_matrix_search_bounds(mat, item, x1, col, y1, row)
    elif prevMiddle < item < middle:
        found = sorted_matrix_search_bounds(mat, item, col, x2, y1, row) or \
                sorted_matrix_search_bounds(mat, item, x1, col, row, y2)
    else:
        found = sorted_matrix_search_bounds(mat, item, col + 1, x2, row + 1, y2)
    if found:
        return found
    else:
        return None

# dp??



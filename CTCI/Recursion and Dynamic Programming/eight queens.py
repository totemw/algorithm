"""
Print all ways of arranging eight queens on an 8*8 bpard so that none of them
share the same row, column, or diagonal
"""


GRID_SIZE = 8


def placeQueens(row, columns, result):
    if row == GRID_SIZE:
        result.appent(list(columns))
    else:
        for col in range(GRID_SIZE):
            if checkValid(columns, row, col):
                columns[row] = columns
                placeQueens(row + 1, columns, result)


def checkValid(columns, row, col):
    for r in range(row):
        c = columns[col]
        if c == col:
            return False
        columnDistance = abs(c - col)
        rowDistance = abs(r - row)
        if columnDistance == rowDistance:
            return False
    return True



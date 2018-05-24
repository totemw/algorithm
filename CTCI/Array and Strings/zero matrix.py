"""
Write an algorithm such that if an element is an M*N matrix,
its entire row and columns are set to 0
"""


def setZeros(m):
    rows = []
    columns = []
    if not m or len(m) == 0 or len(m[0]) == 0:
        return False
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                rows.append(i)
                columns.append(j)
    rows = set(rows)
    columns = set(columns)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i in rows or j in columns:
                m[i][j] = 0
    print m

a = [[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,0,1],[2,3,4,5,6]]
setZeros(a)

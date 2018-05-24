"""
Given an image represented by an N*N matrix, which each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degrees
do it in place?
"""


# swap starting from the outermost layer to inner layer
def rotateMatrix(m):
    if len(m) == 0 or len(m[0]) != len(m):
        return False
    for i in range(len(m) / 2):
        start = i
        end = len(m) - 1 - start
        for j in range(0, end -start):
            tmp = m[start][start + j]
            m[start][start + j] = m[end - j][start]
            m[end - j][start] = m[end][end - j]
            m[end][end - j] = m[start + j][end]
            m[start + j][end] = tmp
            print m

# special example
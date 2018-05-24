"""
"peak" is an element which is greater than or equal to the
adjacent integers and a "valley" is an element which is less
than or equal to the adjacent integers.
Sort the array into an alternating sequence of peaks and valleys
eg. 5 3 1 2 3 -> 5 1 3 2 3

consider:
0 1 2 -> 0 2 1
0 2 1  peak
1 0 2 -> 1 2 0
1 2 0  peak
2 1 0 -> 1 2 0
2 0 1 -> 0 2 1

O(n)
"""
import sys


def maxIndex(array, a, b, c):
    length = len(array)
    aValue = array[a] if 0 <= a < length else -sys.maxint
    bValue = array[b] if 0 <= b < length else -sys.maxint
    cValue = array[c] if 0 <= c < length else -sys.maxint
    maxNum = max(aValue, bValue, cValue)
    if maxNum == aValue:
        return a
    elif maxNum == bValue:
        return b
    else:
        return c


def sortValleyPeaK(array):
    for i in range(1, len(array), 2):
        biggestIndex = maxIndex(array, i - 1, i, i + 1)
        if i != biggestIndex:
            array[i], array[biggestIndex] = array[biggestIndex], array[i]
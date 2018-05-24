"""
Given array-like data structure Listy which lack a size method
it has elementAt(i) - O(1)
beyond the bound - return -1

Given a Listy, which contains sorted, positive integers,
find the index of x, can return any index if x appears multible times

use log n time to guess the size
then binary search partly
"""


def search(listy, value):
    length = 1
    while listy.elementAt(length) != -1 and listy.elementAt(length) < value:
        length *= 2
    return binarySearch(listy, value, length / 2, length)


def binarySearch(listy, value, low, high):
    while low <= high:
        mid = (low + high) / 2
        middle = listy.elementAt(mid)
        if middle == -1 or middle > value:
            high = mid - 1
        elif middle < value:
            low = mid + 1
        else:
             return mid
    return -1

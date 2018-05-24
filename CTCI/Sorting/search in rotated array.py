"""
Given a sorted array of n integers that has been rotated an unknown
number of times ??, write code to find an element in the array
The array is originally sorted in increasing order

Assume only rotate once:
apply binary search
compare the starting point with the middle point
if start < middle - this half is in order
else - the other half is in order
if start == middle -> check the rightmost value
"""


def search(array, left, right, x):
    mid = (left + right) / 2
    if x == array[mid]:
        return mid
    if right < left:
        return -1

    if array[left] < array[mid]:
        if array[left] <= x < array[mid]:
            return search(array, left, mid - 1, x)
        else:
            return search(array, mid + 1, right, x)
    elif array[left] > array[mid]:
        if array[mid] < x <= array[right]:
            return search(array, mid + 1, right, x)
        else:
            return search(array, left, mid - 1, x)
    else:
        if array[mid] != array[right]:
            return search(array, mid + 1, right, x)
        else:
            result = search(array, left, mid - 1, x)
            if result == -1:
                return search(array, mid + 1, right, x)
            else:
                return result
    return -1



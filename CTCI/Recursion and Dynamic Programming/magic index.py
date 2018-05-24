"""
Find a magic index in a sorted array
magic index: A[i] = i
"""


# distinct - binary search
def magicFast(array, lower, upper):
    if lower == upper:
        return None
    middle = lower + (upper - lower) / 2
    if array[middle] == middle:
        return middle
    elif array[middle] > middle:
        return magicFast(array, lower, middle - 1)
    else:
        return magicFast(array, middle + 1, upper)


# non-distinct
def magicIndex(array):
    index = 0
    while index < len(array):
        if index == array[index]:
            return index
        index = max(array[index], index + 1)
    return None


def MagicIndex(array, lower, upper):
    if lower < upper:
        return -1
    middle = lower + (upper - lower) / 2
    middleValue = array[middle]
    if array[middle] == middle:
        return middle
    left = MagicIndex(array, lower, min(middle - 1, middleValue))
    if left >= 0:
        return left
    right = MagicIndex(array, max(middle + 1, middleValue), upper)
    if right >= 0:
        return right

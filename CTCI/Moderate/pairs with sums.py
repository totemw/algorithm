"""
Find all pairs of integers within an array which sum to
a specified value
"""


def pairSum(arr, s):
    values = set()
    for num in arr:
        values.add(num)
    pairs = set()
    for num in arr:
        if s - num in values:
            values.remove(num)
            pairs.add((num, s - num))
    return pairs
"""
Given an array of integers, write a method to find indices m and n
such that if yo sorted elements m through n, the entire array
would be sorted. Minimize n - m


1. find longest increasing subsequence at the beginning and
   the longest increasing subsequence at the end
2. find the first element < middle.first and last element > middle.last
eg left: 1 2 3 7 [10 11
   middle: 8 12
   right: 5 6] 16 18 19
"""


def subsort(arr):
    n = len(arr)
    if not n:
        return 0, 0
    min_so_far = [0] * n
    max_so_far = [0] * n
    max_so_far[0] = arr[0]
    min_so_far[-1] = arr[-1]
    for i in range(1, n):
        max_so_far[i] = max(arr[i], max_so_far[i - 1])
    for i in range(n - 2, -1, -1):
        min_so_far[i] = min(arr[i], min_so_far[i + 1])
    start = 0
    end = n - 1
    while end > 0 and min_so_far[end] == max_so_far[end]:
        end -= 1
    while start < end and min_so_far[start] == max_so_far[start]:
        start += 1
    return start, end

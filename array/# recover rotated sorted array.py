"""
Given a rotated sorted array, recover it to sorted array in-place.
"""

class Solution:
    def recoverRotatedSortedArray(self, arr):
        if arr == None:
            return None
        length = len(arr)
        for i in range(length - 1):
            if arr[i] > arr[i + 1]:
                self.reverse(arr, 0, i)
                self.reverse(arr, i + 1, length - 1)
                self.reverse(arr, 0, length - 1)

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
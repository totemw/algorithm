"""
Given an array and a value, remove all occurrences of that value
 in place and return the new length.

The order of elements can be changed,
and the elements after the new length don't matter.

"""
class Solution:
    def removeElement(self, arr, elem):
        j = len(arr) - 1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] == elem:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
        return j + 1
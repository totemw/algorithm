"""
Given two sorted arrays nums1 and nums2 of size m and n respectively and an int k.
Find the k-th largest element of these arrays.
Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

Example 1:
Input: nums1 = [-2, -1, 3, 5, 6, 8], nums2 = [0, 1, 2, 5, 9], k = 4
Output: 5
Explanation: Union of above arrays will be [-2, -1, 0, 1, 2, 3, 5, 5, 6, 8, 9] and the 4th largest element is 5.

Example 2:
Input: nums1 = [2, 4], nums2 = [6], k = 1
Output: 6
Explanation: union of above arrays will be [2, 4, 6] and the 1st largest element is 6.
You may assume k is always valid, 1 ≤ k ≤ m + n.

Follow-up
Can you do it in O(logk) time?

Median of Two Sorted Arrays: O(log(min(m,n,k))
"""


def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    return self.findKth(A, B, l // 2) if l % 2 == 1 else (self.findKth(A, B, l // 2 - 1) + self.findKth(A, B,
                                                                                                        l // 2)) / 2.0


def findKth(self, A, B, k):
    if len(A) > len(B):
        A, B = B, A
    if not A:
        return B[k]
    if k == len(A) + len(B) - 1:
        return max(A[-1], B[-1])
    i = len(A) // 2
    j = k - i
    if A[i] > B[j]:
        # Here I assume it is O(1) to get A[:i] and B[j:]. In python, it's not but in cpp it is.
        # Rope (data structure)
        return self.findKth(A[:i], B[j:], i)
    else:
        return self.findKth(A[i:], B[:j], j)
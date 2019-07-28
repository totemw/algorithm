"""
Given a collection of intervals, merge all overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

# sort

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)

        result = [intervals[0]]

        for interval in intervals[1:]:
            if result[-1].start <= interval.start and result[-1].end >= interval.end:
                continue
            elif result[-1].end >= interval.start and interval.end >= result[-1].end:
                result[-1].end = interval.end
            else:
                result.append(interval)
        return result
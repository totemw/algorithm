"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.
"""

# greedy / minHeap

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda x: x.start)
        heap = []  # stores the end time of intervals
        for i in intervals:
            if heap and i.start >= heap[0]:
                # means two intervals can use the same room
                heapq.heapreplace(heap, i.end)
            else:
                # a new room is allocated
                heapq.heappush(heap, i.end)
        return len(heap)

class Solution2(object):
    def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)

        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1

                s += 1
            else:
                available += 1
                e += 1

        return numRooms
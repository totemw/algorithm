"""
Given a stream of integers and a window size,
calculate the moving average of all integers in the sliding window.

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

# circular array

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.window = [0] * size
        self.index = 0
        self.currSize = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.window[self.index % self.size] = val
        self.index += 1

        self.sum += val
        self.sum -= self.window[self.index % self.size]

        self.currSize += 1 if self.currSize < self.size else self.currSize

        return float(self.sum) / float(self.currSize)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
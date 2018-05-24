"""
min stack - push pop min in O(1)
"""

import sys
# use another stack to record the min value
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, element):
        if element < self.min():
            self.minstack.append(element)
        self.stack.append(element)

    def pop(self):
        result = self.stack[-1]
        if result == self.min():
            self.minstack.pop()
        self.stack.pop()
        return result

    def min(self):
        if not self.minstack:
            return sys.maxint
        else:
            return self.minstack[-1]

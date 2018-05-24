"""
Implement a stack with min() function,
which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, number):
        self.stack.append(number)
        if len(self.minstack) == 0 or number < self.minstack[-1]:
            self.minstack.append(number)

    def pop(self):
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop()
        return self.stack.pop()

    def min(self):
        return self.minstack[-1]
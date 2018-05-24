"""
As the title described, you should only use two stacks to implement a queue's actions.

The queue should support push(element),
pop() and top() where pop is pop the first(a.k.a front) element in the queue.

Both pop and top methods should return the value of first element.
"""


class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.adjust()
        return self.stack2[len(self.stack2) - 1]

    def pop(self):
        self.adjust()
        return self.stack2.pop()
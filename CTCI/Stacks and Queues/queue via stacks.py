"""
implement a queue by two stacks
"""


class QueueViaStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, element):
        self.stack1.append(element)

    def remove(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop)
        return self.stack2.pop()

"""
SetOfStacks: pop, push, popAt - array of stack
"""


class MultiStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, element):
        if self.stacks and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(element)
        else:
            self.stacks.append([element])

    def pop(self):
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return None
        result = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return result

    def pop_at(self, index):
        if index < 0 or len(self.stacks) < index or not self.stacks[index]:
            return None
        else:
            return self.stacks[index].pop()

"""
describe how you could use a single array to implement three stacks
"""


class ThreeStacks:
    def __init__(self):
        self.array = [None, None, None]
        self.current = [0, 1, 2] # store index in the array

    def push(self, item, stack_number):
        if stack_number not in [0, 1, 2]:
            raise Exception("Bad stack number!")
        while len(self.array) < self.current[stack_number]:
            self.array += [None] * len(self.array)
        self.array[self.current[stack_number]] = item
        self.current[stack_number] += 3

    def pop(self, stack_number):
        if stack_number not in [0, 1, 2]:
            raise Exception("Bad stack number!")
        item = self.array[self.current[stack_number]]
        self.array[self.current[stack_number]] = None
        if self.current[stack_number] > 3:
            self.current[stack_number] -= 3
        return item

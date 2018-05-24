"""
sort a stack such that teh smallest items are on the top
may use another temporary stack
push, pop, peek, isEmpty
"""
class Stack:
    def push(self, element):
        pass

    def pop(self):
        pass

    def isEmpty(self):
        pass

    def peek(self):
        pass


def sortStacks(s):
    tmp = Stack()
    while not s.isEmpty():
        item = s.pop()
        while not tmp.isEmpty() and tmp.peek() > tmp:
            s.push(tmp.pop())
        tmp.push(item)

    while not tmp.isEmpty():
        s.push(tmp.pop())
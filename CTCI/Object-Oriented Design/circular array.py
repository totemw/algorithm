class CircularArray(object):
    def __init__(self, array):
        self.array = array
        self.start = 0

    def rotate(self, i):
        self.start = (self.start + i) % len(self.array)

    def __iter__(self):
        for i in range(self.start, len(self.array)):
            yield self.array[i]
        for i in range(0, self.start):
            yield self.array[i]

    def __getitem__(self, item):
        return self.array[(self.start + item) % len(self.array)]

    def __setitem__(self, key, value):
        self.array[(self.start + key) % len(self.array)] = value

    def __delitem__(self, key):
        index = (self.start + key) % len(self.array)
        del self.array[index]
        if index < self.start:
            self.start -= 1

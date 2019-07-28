"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.

"""

# hash + list

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dict:
            tmp = self.list[-1]
            self.list[-1], self.list[self.dict[val]] = self.list[self.dict[val]], self.list[-1]
            self.dict[tmp] = self.dict[val]
            self.list.pop()
            del self.dict[val]
            return True
        else:
            return False


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.list[random.randint(0, len(self.list) - 1)]
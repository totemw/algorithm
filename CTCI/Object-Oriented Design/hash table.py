"""
hash table using chaining
"""
class Node(object):
    def __init__(self, item, value, next=None):
        self.item = item
        self.value = value
        self.next = next


class HashTable(object):
    def __init__(self, array_size=64):
        self.array = [None for _ in range(array_size)]
        self.count = 0
        self.capacity = 0.75 * array_size

    def add(self, item, value):
        if self.count >= self.capacity:
            self.expand()
        self.count += 1
        new_node = Node(item, value)
        index = hash(item) % len(self.array)
        node = self.array[index]
        if node:
            while node.next:
                node = node.next
            node.next = new_node
        else:
            self.array[index] = new_node

    def lookup(self, item):
        node = self.array[hash(item) % len(self.array)]
        while node:
            if node.item == item:
                return node.value
            node = node.next
        return None

    def delete(self, item):
        index = hash(item) % len(self.array)
        node = self.array[index]
        if node and node.item == item:
            self.count -= 1
            self.array[index] = node.next
        while node.next:
            if node.next.item == item:
                self.count -= 1
                node.next = node.next.next
            node = node.next

    def expand(self):
        new_array = [None for _ in range(2 * len(self.array))]
        self.capacity *= 2
        self.array, prev_array = new_array, self.array
        for node in prev_array:
            while node:
                self.add(node.item, node.value)
                node = node.next

    def __len__(self):
        return self.count

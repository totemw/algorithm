"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
"""

# dictionary + keep order (dequeue / double linked list)

class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        if key in self.dict:
            self._remove(self.dict[key])
            self._add(self.dict[key])
            return self.dict[key].value
        else:
            return -1

    def put(self, key, value):
        newNode = Node(key, value)

        if key in self.dict:
            self._remove(self.dict[key])

        self._add(newNode)
        self.dict[key] = newNode

        if len(self.dict) > self.capacity:
            del self.dict[self.head.next.key]
            self._remove(self.head.next)


    def _remove(self, node):
        prevNode = node.prev
        node = node.next
        prevNode.next = node
        node.prev = prevNode

    def _add(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
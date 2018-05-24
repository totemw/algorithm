"""
Design and build a "least recently used" cache, which evicts the last
recently used item. The cache should map from keys to values with a max size.
When it is full, it should evict the least recently used item.
You can assume the keys are integers and the values are strings

- Insert (key, value) pair
- retrieving value by key
- finding least recently used
- update most recently used
- eviction

we use a doubled linked list & hash map
- insert node into linked list, insert (key, node) into hash table
- Look up node in hash table and return value
- least node - found at the end of the linked list
- update - move node to front of linked list
- eviction - remove tail of linked list & key from hash table

"""


class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Cache:
    def __init__(self, size):
        self.maxCacheSize = size
        self.map = {}
        self.head = None
        self.tail = None

    def remove(self, node):
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        if node == self.tail:
            self.tail = node.prev
        if node == self.head:
            self.head = node.next

    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def getValue(self, key):
        if key in self.map:
            item = self.map[key]
        else:
            return None
        if item != self.head:
            self.remove(item)
            self.insert(item)
        return item.value

    def removeKey(self, key):
        node = self.map[key]
        self.remove(node)
        del self.map[key]
        return True

    def setKeyValue(self, key, value):
        if key in self.map:
            self.remove(key)
        if len(self.map.keys()) >= self.maxCacheSize and self.tail:
            self.remove(self.tail.key)
        node = LinkedListNode(key, value)
        self.insert(node)
        self.map[key] = node

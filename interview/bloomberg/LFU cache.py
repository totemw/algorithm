"""
Design and implement a data structure for Least Frequently Used (LFU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

"""


# 2 dictionary (nodeMap & freqMap : each freq <-> Dlist) + keep order (dequeue / double linked list)

class Node:
    def __init__(self, k, v, f):
        self.key = k
        self.value = v
        self.freq = f
        self.prev = None
        self.next = None


class LFUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.min = 1
        self.nodeMap = {}
        self.freqMap = {}
        self.record = None

    def get(self, key):
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self._update(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self._update(node)
        else:
            newNode = Node(key, value, 1)
            self.nodeMap[key] = newNode
            self._checkFreqMap(1)
            head, tail = self.freqMap[1]
            if head.next != tail:
                self.min = 1
            self.record = newNode
            self._add(newNode, tail)

        if len(self.nodeMap) > self.capacity:
            head, tail = self.freqMap[self.min]
            del self.nodeMap[head.next.key]
            self._remove(head.next)
            if head.next == tail:
                keys = []
                for key in self.freqMap.keys():
                    keys.append(key)
                keys.sort()
                for key in keys:
                    head, tail = self.freqMap[key]
                    if head.next != tail and head.next != self.record:
                        self.min = key

        if len(self.nodeMap) == 0:
            self.min = 1

    def _update(self, node):
        prevHead, prevTail = self.freqMap[node.freq]
        node.freq += 1
        self._remove(node)
        if prevHead.next == prevTail:
            self.min = node.freq
        self._checkFreqMap(node.freq)
        currHead, currTail = self.freqMap[node.freq]
        self._add(node, currTail)
        self.nodeMap[node.key] = node

    def _remove(self, node):
        prevNode = node.prev
        node = node.next
        prevNode.next = node
        node.prev = prevNode

    def _add(self, node, tail):
        prevNode = tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = tail
        tail.prev = node

    def _checkFreqMap(self, i):
        if i not in self.freqMap:
            head = Node(0, 0, 0)
            tail = Node(0, 0, 0)
            head.next = tail
            tail.prev = head
            self.freqMap[i] = (head, tail)
        else:
            return

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""




"put","get","get","get","put",
"put","put","get","put","get",
"get","put","put","get","put",



[2,14],[1],[5],[4],[11,4],
[12,24],[5,18],[13],[7,23],[8],
[12],[3,27],[2,12],[5],[2,9],
"""
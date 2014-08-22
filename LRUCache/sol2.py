# DoubleLinked List solution
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head = None
        self.tail = None
    def remove(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if self.head == node:
            node.next.prev = None
            self.head = node.next
            return
        if self.tail == node:
            node.prev.next = None
            self.tail = node.prev
            return
        node.next.prev = node.prev
        node.prev.next = node.next
        return
    def removeLast(self):
        self.remove(self.tail)
    def addToFront(self, node):
        if not self.head:
            self.head = self.tail = node
            node.prev = None
            node.next = None
            return
        node.next = self.head
        node.prev = None
        node.next.prev = node
        self.head = node

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.cache = DList()

    # @return an integer
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.cache.remove(node)
        self.cache.addToFront(node)
        return node.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            node = self.map[key]
            self.cache.remove(node)
            node.value = value
            self.cache.addToFront(node)
        elif self.size < self.capacity:
            self.size += 1
            node = Node(key, value)
            self.map[key] = node
            self.cache.addToFront(node)
        else:
            lastKey = self.cache.tail.key
            del self.map[lastKey]
            self.cache.removeLast()
            node = Node(key, value)
            self.map[key] = node
            self.cache.addToFront(node)

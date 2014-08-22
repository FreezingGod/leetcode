# TLE on large test case
# main bottleneck is self.list.remove(entry), which use O(n) time
class LRUCache:
    class CacheEntry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.map = {}

    # @return an integer
    def get(self, key):
        if key not in self.map:
            return -1
        self.moveToHead(key)
        return self.map[key].value

    def moveToHead(self, key):
        entry = self.map[key]
        self.list.remove(entry)
        self.list.insert(0, entry)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.map:
            self.map[key].value = value
            self.moveToHead(key)
        elif len(self.list) < self.capacity:
            entry = LRUCache.CacheEntry(key, value)
            self.map[key] = entry
            self.list.insert(0, entry)
        else:
            entry = LRUCache.CacheEntry(key, value)
            toRemove = self.list.pop()
            del self.map[toRemove.key]
            self.map[key] = entry
            self.list.insert(0, entry)

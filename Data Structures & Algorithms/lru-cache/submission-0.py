class Node:
    def __init__(self, key, val):
        self.key = key
        self. val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right # LRU
        self.right.prev = self.left # MRU
        

    def insert(self, node):
        prev = self.right.prev
        curr = node
        prev.next = curr
        curr.prev = prev
        curr.next = self.right
        self.right.prev = curr

    def remove(self, node):
        curr = node
        prev = curr.prev
        nxt = curr.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to remove and update to MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # check the capacity versus size
        if len(self.cache) > self.cap:
            # remove & delete LRU LL & Hash
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

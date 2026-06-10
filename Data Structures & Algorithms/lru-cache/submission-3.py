class Node:
    def __init__(self,key=None, val=None, prev=None, next=None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.removeNode(node)
            self.addNode(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.addNode(new_node)
            self.size += 1
        if self.size > self.capacity:
            last_node = self.tail.prev
            self.removeNode(last_node)
            self.cache.pop(last_node.key)
            self.size -= 1

    def addNode(self, node):
        old_first = self.head.next
        node.next = old_first
        old_first.prev = node
        self.head.next = node
        node.prev = self.head
    
    def removeNode(self, node):
        before_node = node.prev
        after_node = node.next
        before_node.next = after_node
        after_node.prev = before_node
        node.next = None
        node.prev = None
        

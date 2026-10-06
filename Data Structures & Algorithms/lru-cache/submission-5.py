class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = {}
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, key):
        newNode = self.cache[key]
        newNode.prev = self.right.prev
        self.right.prev.next = newNode
        newNode.next = self.right
        self.right.prev = newNode

    def remove(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(key)
        self.insert(key)
        return self.cache[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(key)
        
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(key)

        if self.size < len(self.cache):
            leastNode = self.left.next
            self.remove(leastNode.key)
            del self.cache[leastNode.key] 

        

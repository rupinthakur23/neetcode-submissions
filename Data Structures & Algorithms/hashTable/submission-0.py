class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hash = [ListNode(-1, -1) for _ in range(self.capacity)]
    
    def hashing(self, key):
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hashing(key)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
                return
            curr = curr.next
        
        curr.next = ListNode(key, value)
        self.size +=1
        if (self.size / self.capacity) >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hashing(key)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hashing(key)
        curr = self.hash[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                self.size -=1
                return True
            curr = curr.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        self.newHash = [ListNode(-1, -1) for _ in range(self.capacity)]
        self.oldHash = self.hash

        for bucket in self.oldHash:
            curr = bucket.next
            while curr:
                newNode = ListNode(curr.key, curr.value)
                newIndex = self.hashing(curr.key)
                newNode.next = self.newHash[newIndex].next
                self.newHash[newIndex].next = newNode
                curr = curr.next
        self.hash = self.newHash





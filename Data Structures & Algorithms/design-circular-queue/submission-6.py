class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = k
        self.front = Node(-1)
        self.back = Node(-1)
        self.front.next = self.back
        self.back.prev = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        node = Node(value)
        node.prev = self.back.prev
        self.back.prev.next = node
        node.next = self.back
        self.back.prev = node
        self.size -=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next.next.prev = self.front
        self.front.next = self.front.next.next
        self.size +=1
        return True

    def Front(self) -> int:
        if self.front.next == self.back:
            return -1    
        return self.front.next.val
        
    def Rear(self) -> int:
        if self.back.prev == self.front:
            return -1
        return self.back.prev.val
        
    def isEmpty(self) -> bool:
        return self.size == self.capacity 

    def isFull(self) -> bool:
        return self.size <= 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
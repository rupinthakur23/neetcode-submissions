class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.right = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            newNode = Node(value)
            self.right.prev.next = newNode
            newNode.prev = self.right.prev
            newNode.next = self.right
            self.right.prev = newNode
            self.size -=1
            return True
        return False
        
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next
            self.size +=1
            return True
        return False
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.left.next.val 
        return -1      
        
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.right.prev.val
        return -1

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
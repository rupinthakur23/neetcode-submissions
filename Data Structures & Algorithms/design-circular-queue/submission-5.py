class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            node = ListNode(value)
            self.right.prev.next = node
            node.prev = self.right.prev
            node.next = self.right
            self.right.prev = node
            self.size -= 1
            return True
        return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.left.next.next.prev = self.left
            self.left.next = self.left.next.next
            self.size += 1
            return True
        
        return False

    def Front(self) -> int:
        return self.left.next.val
        
    def Rear(self) -> int:
        return self.right.prev.val        

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
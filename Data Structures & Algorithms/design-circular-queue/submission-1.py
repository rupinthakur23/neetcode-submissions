class Node:
    def __init__(self, val, nextNode = None , prevNode = None):
        self.val = val
        self.next = nextNode
        self.prev = prevNode

class MyCircularQueue:

    def __init__(self, k: int):
        self.head, self.tail = None, None
        self.size = k
        self.length = 0

    def enQueue(self, value: int) -> bool:
        newNode = Node(value)
        if not self.head and not self.tail:
            self.head, self.tail = newNode, newNode
            newNode.next = newNode
        else:
            if self.length >= self.size:
                return False
            else:
                self.tail.next = newNode
                self.tail = self.tail.next 
                self.tail.next = self.head
        self.length +=1
        return True
        
    def deQueue(self) -> bool:
        if self.length == 0:
            return False
        else:
            if self.length == 1:
                self.head, self.tail = None, None
            else:
                self.tail.next = self.head.next
                self.head = self.tail.next
            self.length -=1
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1
        

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.size == self.length 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
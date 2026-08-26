class ListNode:
    def __init__(self, value, next_node = None):
        self.val = value
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
  
    def get(self, index: int) -> int:
        current = self.head
        count = -1
        while(current):
            if (count == index):
                return current.val
            current = current.next
            count+=1 
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.head
        counter = 0

        while(counter < index and current):
            counter+= 1
            current = current.next

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False


    def getValues(self) -> List[int]:
        result = []
        current = self.head.next
        while(current):
            result.append(current.val)
            current = current.next
        return result
        

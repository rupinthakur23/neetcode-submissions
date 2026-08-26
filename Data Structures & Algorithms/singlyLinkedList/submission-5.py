class ListNode:
    def __init__(self, val, nextNode = None):
        self.value = val
        self.next = nextNode

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        counter = 0
        curr = self.head.next
        while curr:
            if counter == index:
                return curr.value
            curr = curr.next
            counter +=1
        
        return -1

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode

        
    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        
    def remove(self, index: int) -> bool:
        counter = 0
        curr = self.head

        while counter < index and curr:
            counter +=1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr != None:
            result.append(curr.value)
            curr = curr.next
        return result
        

class ListNode:
    def __init__(self,val, nextnode = None):
        self.val = val
        self.next = nextnode

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        counter = 0
        curr = self.head.next

        while curr:
            if counter == index:
                return curr.val
            counter += 1
            curr = curr.next

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
        self.tail = self.tail.next

    
    def remove(self, index: int) -> bool:
        counter = 0
        curr = self.head

        while curr and counter < index:
            counter +=1
            curr = curr.next
        
        if curr and curr.next:
            if self.tail == curr.next:
                self.tail = curr
            curr.next = curr.next.next
            return True
        
        return False

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

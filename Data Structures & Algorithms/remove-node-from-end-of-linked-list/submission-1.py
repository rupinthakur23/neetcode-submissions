# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        counter = 0
        current = head
        while(current):
            counter += 1
            current = current.next
        
        index = 0
        runner = dummyNode
        
        while(index < (counter - n)):
            runner = runner.next
            index +=1
        
        runner.next = runner.next.next
        return dummyNode.next
        

        

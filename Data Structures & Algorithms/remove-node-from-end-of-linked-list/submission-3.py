# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        dummyNode.next = head
        curr = head
        length = 0
        counter = 1

        while curr:
            length +=1
            curr = curr.next
        
        index = length - n + 1

        curr = dummyNode

        while curr and curr.next and counter < index:
            curr = curr.next
            counter +=1
        
        curr.next = curr.next.next
        return dummyNode.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        dummy = ListNode(-1, head)
        
        size = 0
        while curr:
            size +=1
            curr = curr.next
        
        counter = 0
        curr = dummy
        
        while counter < (size - n):
            curr = curr.next
            counter +=1
        
        curr.next = curr.next.next

        return dummy.next

        
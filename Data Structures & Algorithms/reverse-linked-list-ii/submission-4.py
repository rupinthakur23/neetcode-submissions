# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy

        for _ in range(left - 1):
            curr = curr.next
        
        oldPrev = curr
        prev = None
        curr = curr.next

        for _ in range(left, right + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        
        oldPrev.next.next = curr
        oldPrev.next = prev

        return dummy.next
        


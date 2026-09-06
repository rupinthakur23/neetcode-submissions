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
        
        prevNode = curr
        curr = curr.next
        prev = None

        for _ in range(left, right + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        prevNode.next.next = curr
        prevNode.next = prev

        return dummy.next

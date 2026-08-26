# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prevPointer = None
        curr = head
        nextPointer = head.next

        while curr:
            nextPointer = curr.next
            curr.next = prevPointer
            prevPointer = curr
            curr = nextPointer

        return prevPointer
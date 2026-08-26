# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr , prev = slow.next, None
        slow.next = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        left, right = head, prev

        while left and right:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left, right = temp1, temp2





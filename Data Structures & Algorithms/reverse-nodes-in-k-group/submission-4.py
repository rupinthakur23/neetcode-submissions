# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        before = dummy

        while True:
            kth = self.kthNode(before, k)
            if not kth:
                break
            
            prev = before
            curr = before.next

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = before.next
            before.next.next = curr
            before.next = prev
            before = tmp
        return dummy.next

    def kthNode(self, curr, k):
        size = k
        while curr and size > 0:
            curr = curr.next
            size -=1

        return curr



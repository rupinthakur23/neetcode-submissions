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
            kthNode = self.getkthNode(before, k)
            if not kthNode:
                break
            
            afterKth = kthNode.next
            curr = before.next
            prev = kthNode.next

            while curr != afterKth:
                nxtNode = curr.next
                curr.next = prev
                prev = curr
                curr = nxtNode
            
            tmp = before.next
            before.next = prev
            before = tmp
        
        return dummy.next


    def getkthNode(self, curr, k):
        while k > 0 and curr:
            curr = curr.next
            k -=1
        
        return curr
        

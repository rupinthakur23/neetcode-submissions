# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        groupPrev = dummy

        while True:
            kth = self.kthnode( groupPrev, k)
            if not kth:
                break
            nxtNode = kth.next

            prev = kth.next
            curr = groupPrev.next

            while curr != nxtNode:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def kthnode(self, curr, k):
        while k >0 and curr:
            curr = curr.next
            k -=1
        return curr
        
            

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        beforePrev = dummy

        while True:
            kthNode = self.findKthNode(beforePrev, k)
            if not kthNode:
                break
            kthNodeNext = kthNode.next

            curr = beforePrev.next
            prev = kthNodeNext

            while curr!= kthNodeNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = beforePrev.next
            beforePrev.next = prev
            beforePrev = temp
        
        return dummy.next

    def findKthNode(self, node, k):
        while k > 0 and node:
            node = node.next
            k -=1
        
        return node

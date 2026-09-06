# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevNode = dummy

        while True:
            kthNode = self.getKthNode(prevNode, k)
            if not kthNode:
                break
            
            afterkthNode = kthNode.next
            prev = afterkthNode
            curr = prevNode.next

            while curr != afterkthNode:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            tmp = prevNode.next
            prevNode.next = prev
            prevNode = tmp
        
        return dummy.next


    def getKthNode(self, node, k):
        size = k
        while node and size > 0:
            node = node.next
            size -=1
        return node
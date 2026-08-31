# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1, head)
        counter = 1
        curr = head
        length = 0

        while curr:
            length +=1
            curr = curr.next
        
        curr = dummyNode

        while curr and counter < (length - n + 1):
            curr = curr.next
            print(curr.val)
            counter +=1
        
        curr.next = curr.next.next

        return dummyNode.next

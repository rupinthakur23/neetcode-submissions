# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr =dummy
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, [node.val, i, node])
        
        while minHeap:
            val, index, node = heapq.heappop(minHeap)

            curr.next = ListNode(val)
            curr = curr.next

            if node.next:
                heapq.heappush(minHeap, [node.next.val, index, node.next])
        
        return dummy.next





        

        
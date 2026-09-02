# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode(-1)
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heap.append([node.val, i, node])
        
        heapq.heapify(heap)

        while heap:
            val, index, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next

            if node.next:
                heapq.heappush(heap, [node.next.val, index, node.next])
        
        return dummy.next


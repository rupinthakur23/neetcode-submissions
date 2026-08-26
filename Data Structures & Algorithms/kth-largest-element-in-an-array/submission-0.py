class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        index = 0
        result = heap[0]

        while index < k:
            result = heapq.heappop(heap)
            index+= 1
        

        return -result

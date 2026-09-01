class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap, result = [], []
        l = 0

        for r in range(len(nums)):
            heapq.heappush(maxHeap, [-nums[r], r])

            while maxHeap and maxHeap[0][1] <l:
                heapq.heappop(maxHeap)

            if (r - l + 1) >= k:
                result.append(-maxHeap[0][0])
                l+=1
            
        
        return result


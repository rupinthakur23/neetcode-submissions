class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result, queue = [], deque()
        l = 0

        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            if queue and queue[0] < l:
                queue.popleft()

            queue.append(r)

            if (r - l + 1) == k:
                result.append(nums[queue[0]])
                l +=1
        
        return result
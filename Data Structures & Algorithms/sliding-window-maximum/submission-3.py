class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        q = deque()
        output = []
        for right in range (len(nums)):
            while(q and nums[right] > nums[q[-1]]):
                q.pop()
            q.append(right)

            if left > q[0]:
                q.popleft()
            
            
            if(right - left + 1 >=k):
                output.append(nums[q[0]])
                left +=1
        return output

        
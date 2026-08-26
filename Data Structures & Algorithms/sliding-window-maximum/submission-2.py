class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        l, r, = 0,0
        output = []

        while(r< len(nums)):
            while(window and nums[window[-1]] < nums[r]):
                window.pop()
            window.append(r)

            if (l > window[0]):
                window.popleft()

            if (r + 1 >= k):
                output.append(nums[window[0]])
                l+=1
            r+=1
        
        return output
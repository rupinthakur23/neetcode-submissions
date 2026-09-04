class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right, result = max(nums), sum(nums), float('inf')

        def calculateArrays(capacity):
            total, subArrays = 0, 1
            for num in nums:
                total += num
                if total > capacity:
                    subArrays +=1
                    total = num
            
            return subArrays

        while left <= right:
            mid = left + (right - left)//2

            totalArrays = calculateArrays(mid)

            if totalArrays <= k:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return result
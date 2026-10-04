class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right, result = max(nums), sum(nums), float('inf')

        def calculateArrays(capacity):
            total, count = 0, 1

            for num in nums:
                total += num
                if total > capacity:
                    count +=1
                    total = num
            return count

        while left <= right:
            mid = left + (right - left)//2

            totalArays = calculateArrays(mid)

            if totalArays <= k:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result 
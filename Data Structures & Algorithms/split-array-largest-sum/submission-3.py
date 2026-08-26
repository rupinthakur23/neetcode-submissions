class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        def calaculateSplits(mid):
            count, total  = 1, 0

            for weight in nums:
                total += weight

                if total > mid:
                    count +=1
                    total = weight
            
            return count

        while left <= right:
            mid = left + ((right - left)//2)

            split = calaculateSplits(mid)

            if split <= k:
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
        return result
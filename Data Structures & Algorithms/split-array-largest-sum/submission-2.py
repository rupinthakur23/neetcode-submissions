class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        def calculateSplits(mid):
            total, split = 0 ,1 

            for num in nums:
                total += num

                if total > mid:
                    split +=1
                    total = num
            return split

        while left <= right:
            mid = left + ((right - left) //2)

            splits = calculateSplits(mid)

            if splits <= k:
                right = mid - 1
                result = min(result, mid)
            else:
                left = mid + 1
        
        return result
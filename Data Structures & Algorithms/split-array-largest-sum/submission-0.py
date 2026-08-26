class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        def isSplit(capacity):
            splits, output = 1, 0

            for num in nums:
                output+= num
                if(output > capacity):
                    splits+=1
                    output = num
            
            return splits <= k  

        while(left <= right):
            mid = (left + right)//2

            if(isSplit(mid)):
                result = min(mid, result)
                right = mid - 1
            else:
                left = mid + 1

    
        return result
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        result = right

        def splitCount(total):
            split, output = 1, 0

            for num in nums:
                output += num

                if output > total:
                    split += 1
                    output = num
            
            return split
    

        while left <= right:
            mid = left + ((right - left) //2)
            print(mid)

            if splitCount(mid) <=k:
                right = mid - 1
                result = min(mid, result)
            else:
                left = mid + 1

        return result
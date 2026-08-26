class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result, count = nums[0], 1

        for num in range(1, len(nums)):
            if nums[num] == result:
                count +=1
            else:
                if(count > 0):
                    count -=1
                else:
                    result = nums[num]
                    count +=1
        return result
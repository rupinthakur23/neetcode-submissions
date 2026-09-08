class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, result = 0, 0

        for num in nums:
            if num == result:
                count +=1
            else:
                if count <=0:
                    result = num
                    count +=1
                else:
                    count -=1
        
        return result

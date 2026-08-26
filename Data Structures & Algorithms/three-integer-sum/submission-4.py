class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for index in range(0, len(nums) - 2):
            if(index > 0 and nums[index] == nums[index - 1]):
                continue
        
            left, right = index + 1, len(nums) - 1
            while(left < right):
                total = nums[index] + nums[left] + nums[right]
                if(total > 0):
                    right -=1
                elif total < 0:
                    left +=1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left +=1
                    right -=1

                    while(left < right and nums[left] == nums[left -1]):
                        left +=1
                    
        return result

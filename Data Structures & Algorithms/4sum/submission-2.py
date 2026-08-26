class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()

        for index in range(0, len(nums) - 3):
            if(index > 0 and nums[index] == nums[index - 1]):
                continue
            
        
            for start in range(index + 1, len(nums) - 2):
                if(start > index + 1 and nums[start] == nums[start - 1]):
                    continue     
                left, right = start + 1, len(nums) - 1
                while(left < right):
                    total = nums[index] + nums[start] + nums[left] + nums[right]
                    if(total > target):
                        right -=1
                    elif total < target:
                        left +=1
                    else:
                        result.append([nums[start], nums[index], nums[left], nums[right]])
                        left +=1
                        right -=1

                        while(left < right and nums[left] == nums[left -1]):
                            left +=1        
        return result
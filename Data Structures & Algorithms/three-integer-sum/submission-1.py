class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        start = 0
        nums.sort()

        while(start < len(nums) - 2):
            left = start + 1
            right = len(nums) - 1

            if (start >0 and nums[start] == nums[start - 1]):
                start += 1
                continue

            while(left < right):
                if(nums[start] + nums[right] + nums[left] > 0):
                    right -=1
                elif(nums[start] + nums[right] + nums[left] < 0):
                    left +=1
                else:
                    result.append([nums[start], nums[left], nums[right]])
                    left +=1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
            
            start += 1
        
        return result




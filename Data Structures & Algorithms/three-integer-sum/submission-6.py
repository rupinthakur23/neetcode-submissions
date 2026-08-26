class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for pointer in range(0, len(nums) -2):
            if pointer > 0 and nums[pointer] == nums[pointer - 1]:
                continue
            left, right = pointer + 1, len(nums) - 1

            while left < right:
                if nums[pointer] + nums[left] + nums[right] > 0:
                    right -=1
                elif nums[pointer] + nums[left] + nums[right] < 0:
                    left +=1
                else:
                    result.append([nums[pointer], nums[left], nums[right]])
                    left +=1
                    right -=1

                    while left < right and nums[left] == nums[left - 1]:
                        left +=1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
                                          
        
        return result

        
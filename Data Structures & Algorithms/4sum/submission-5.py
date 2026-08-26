class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []

        for pointer1 in range(0, len(nums) -3):
            if pointer1 > 0 and nums[pointer1] == nums[pointer1 - 1]:
                continue
            for pointer2 in range(pointer1 + 1, len(nums) -2):
                if pointer2 > pointer1 + 1 and nums[pointer2] == nums[pointer2 - 1]:
                    continue
                left, right = pointer2 + 1, len(nums) - 1

                while left < right:
                    if nums[pointer1] + nums[pointer2] + nums[left] + nums[right] > target:
                        right -=1
                    elif nums[pointer1] + nums[pointer2] + nums[left] + nums[right] < target:
                        left +=1
                    else:
                        result.append([nums[pointer1], nums[pointer2], nums[left], nums[right]])
                        left +=1
                        right -=1

                        while left < right and nums[left] == nums[left - 1]:
                            left +=1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -=1                                   
        
        return result

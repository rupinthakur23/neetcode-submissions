import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        
        def quickSelect(l,r):
            pivot = random.randint(l,r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            pointer = l

            for index in range(l,r):
                if nums[index] <= nums[r]:
                    nums[pointer], nums[index] = nums[index], nums[pointer]
                    pointer += 1
            
            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer > k:
                return quickSelect(l, pointer -1)
            elif pointer < k:
                return quickSelect(pointer + 1, r)
            else:
                return nums[pointer]
        
        return quickSelect(0, len(nums)-1)

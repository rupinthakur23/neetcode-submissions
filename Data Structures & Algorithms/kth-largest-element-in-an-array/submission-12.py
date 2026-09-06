import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot_idx = random.randint(l,r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = r
            pointer = l
            for i in range(l, r):
                if nums[pivot] >= nums[i]:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer +=1
            
            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]

            if pointer == k:
                return nums[pointer]
            elif pointer > k:
                return quickSelect(l, pointer -1)
            else:
                return quickSelect(pointer + 1, r)

        return quickSelect(0, len(nums) - 1)
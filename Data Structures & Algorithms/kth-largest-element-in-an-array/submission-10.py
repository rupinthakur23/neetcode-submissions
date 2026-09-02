class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(left, right):
            pointer, pivot = 0, right

            for r in range(pivot):
                if nums[r] <= nums[pivot]:
                    nums[pointer], nums[r] = nums[r], nums[pointer]
                    pointer +=1

            nums[pointer], nums[pivot] = nums[pivot], nums[pointer]

            if pointer == len(nums) - k:
                return nums[pointer]
            elif pointer > len(nums) - k:
                return quickSelect(0, pointer - 1)
            else:
                return quickSelect(pointer + 1, right)


        return quickSelect(0, len(nums) - 1)
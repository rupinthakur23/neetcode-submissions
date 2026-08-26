from typing import List
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # convert to kth smallest index

        def quickSelect(l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = nums[r]
            pointer = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[pointer], nums[i] = nums[i], nums[pointer]
                    pointer += 1

            nums[pointer], nums[r] = nums[r], nums[pointer]

            if pointer < k:
                return quickSelect(pointer + 1, r)
            elif pointer > k:
                return quickSelect(l, pointer - 1)
            else:
                return nums[pointer]

        return quickSelect(0, len(nums) - 1)
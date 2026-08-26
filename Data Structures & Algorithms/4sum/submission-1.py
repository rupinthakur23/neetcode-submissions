class Solution:
    def fourSum(self, nums, target):
        nums.sort()

        def twoSum(nums, target, start):
            res = []
            left, right = start, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right]

                if total == target:
                    res.append([nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif total < target:
                    left += 1
                else:
                    right -= 1

            return res

        def kSum(nums, target, k, start):
            res = []

            if k == 2:
                return twoSum(nums, target, start)

            for i in range(start, len(nums) - k + 1):

                if i > start and nums[i] == nums[i - 1]:
                    continue

                subsets = kSum(nums, target - nums[i], k - 1, i + 1)

                for subset in subsets:
                    res.append([nums[i]] + subset)

            return res

        return kSum(nums, target, 4, 0)
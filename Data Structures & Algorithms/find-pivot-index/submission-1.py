class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        prefixSum= 0

        for i in range(len(nums)):
            prefixSum += nums[i]
            prefix.append(prefixSum)

        for i in range(len(nums)):
            leftIndex = prefix[i - 1] if i >0 else 0
            if leftIndex == (prefix[-1] - prefix[i]):
                return i

        return -1


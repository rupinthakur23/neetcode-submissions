class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = []
        total = 0

        for num in nums:
            total += num
            prefixSum.append(total)

        
        for index, num in enumerate(nums):
            leftIndex = prefixSum[index - 1] if index >0 else 0
            if leftIndex == (prefixSum[-1] - prefixSum[index]):
                return index
        
        return - 1


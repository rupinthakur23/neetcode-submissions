class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result, subset = 0, 0

        def dfs(index, xor):
            if index >= len(nums):
                 return xor
            
            left = dfs(index + 1, xor ^ nums[index])

            right = dfs(index + 1, xor)

            return left + right


        return dfs(0, 0)


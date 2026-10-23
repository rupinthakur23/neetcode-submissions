class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        def backtracking(total, index):
            nonlocal result
            if index >= len(nums):
                result += total
                return
            
            backtracking(total ^ nums[index], index + 1)
            backtracking(total, index + 1)
            

        backtracking(0, 0)
        return result
        
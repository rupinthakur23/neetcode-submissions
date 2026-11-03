class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        def backtracking(i, total):
            nonlocal result

            if i == len(nums):
                result += total
                return
            
            backtracking(i + 1, total ^ nums[i])
            backtracking(i + 1, total)



        backtracking(0,0)
        return result
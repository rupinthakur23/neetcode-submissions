class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def dfs(total, index):
            nonlocal res
            if index >= len(nums):
                res += total
                return
              
            dfs(total ^ nums[index], index + 1)
            dfs( total, index + 1)
        

        dfs(0, 0)
        return res

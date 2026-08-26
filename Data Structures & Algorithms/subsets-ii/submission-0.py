class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, subsets = [], []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                result.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i = i +1
            
            dfs(i + 1)
    

        dfs(0)
        return result
        
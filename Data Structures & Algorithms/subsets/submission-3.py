class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, curset = [], []

        def dfs(subset, curset, index):
            if index >= len(nums):
                subset.append(curset.copy())
                return
            
            curset.append(nums[index])
            dfs(subset, curset, index + 1)
            curset.pop()
            dfs(subset, curset, index + 1)
            
        dfs(subset, curset, 0)
        return subset
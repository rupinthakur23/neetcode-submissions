class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currset = [], []

        def dfs(currset, index):
            if index >= len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[index])

            dfs(currset, index + 1)

            currset.pop()

            dfs(currset, index + 1)
        
        dfs(currset, 0)
        return subset
    
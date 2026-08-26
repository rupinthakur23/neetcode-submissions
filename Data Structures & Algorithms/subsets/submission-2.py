class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, currset = [], []

        def dfs(index):
            if index >= len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[index])

            dfs( index + 1)

            currset.pop()

            dfs( index + 1)
        
        dfs(0)
        return subset
    
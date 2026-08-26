class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset, currset = [], []

        def dfs(index):
            if index >= len(nums):
                subset.append(currset.copy())
                return
            
            currset.append(nums[index])

            dfs( index + 1)

            currset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index+=1

            dfs( index + 1)
        
        dfs(0)
        return subset
    
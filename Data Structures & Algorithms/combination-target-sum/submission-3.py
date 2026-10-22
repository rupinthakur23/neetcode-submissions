class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultSet, currSet = [], []

        def dfs(currSet, index):

            if sum(currSet) == target:
                resultSet.append(currSet.copy())
                return
            
            if sum(currSet) > target:
                return

            for index in range(index, len(nums)):
                currSet.append(nums[index])

                dfs(currSet, index)

                currSet.pop()
        
        dfs(currSet, 0)
        return resultSet

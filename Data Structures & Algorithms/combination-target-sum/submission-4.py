class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        resultSet, currSet = [], []

        def dfs(total, index):

            if total == target:
                resultSet.append(currSet.copy())
                return
            
            if total > target:
                return

            for index in range(index, len(nums)):
                currSet.append(nums[index])

                dfs(total + nums[index], index)

                currSet.pop()
        
        dfs(0, 0)
        return resultSet

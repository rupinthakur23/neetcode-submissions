class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, subset = [], []


        def dfs(index):
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            if index >= len(nums) or sum(subset) > target:
                return


            for i in range(index, len(nums)):
                subset.append(nums[i])

                dfs(i)

                subset.pop()


        dfs(0)

        return result
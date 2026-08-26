class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, subset = [], []
        nums.sort()


        def dfs(index, total):
            if total == target:
                result.append(subset.copy())
                return
            
            if index >= len(nums) or total > target:
                return


            for i in range(index, len(nums)):
                subset.append(nums[i])

                dfs(i,  total + nums[i])

                subset.pop()


        dfs(0, 0)

        return result
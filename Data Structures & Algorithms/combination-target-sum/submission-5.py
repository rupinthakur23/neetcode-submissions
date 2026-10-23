class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        subset, currset = [], []

        def backtracking(total, index):
            if total == target:
                subset.append(currset.copy())
                return
            
            if total > target:
                return
            
            for i in range(index, len(nums)):
                currset.append(nums[i])
                backtracking(total + nums[i], i)
                currset.pop()
        
        backtracking(0, 0)
        return subset
        
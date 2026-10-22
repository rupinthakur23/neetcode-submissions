class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        currset, subset = [], []

        def backtracking(currset, subset, index):
            if index >= len(nums):
                subset.append(currset.copy())
                return
            currset.append(nums[index])
            backtracking(currset, subset, index + 1)
            currset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index +=1
            backtracking(currset, subset, index + 1)
        backtracking(currset, subset, 0)
        return subset

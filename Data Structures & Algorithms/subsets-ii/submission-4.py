class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        currSet, resSet = [], []

        def backtracking(i):
            if i == len(nums):
                resSet.append(currSet.copy())
                return
            
            currSet.append(nums[i])

            backtracking(i + 1)

            while (i + 1 < len(nums)) and nums[i] == nums[i + 1]:
                i +=1

            currSet.pop()
            backtracking(i + 1)

        backtracking(0)
        return resSet
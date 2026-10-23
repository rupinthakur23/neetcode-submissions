class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, currset = [], []

        def backtracking(subsets, currset, index):
            if index >= len(nums):
                subsets.append(currset.copy())
                return
            
            currset.append(nums[index])

            backtracking(subsets, currset, index + 1)
            currset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index +=1
            backtracking(subsets, currset, index + 1)


        backtracking(subsets, currset, 0)
        return subsets
        
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets, currset = [], []

        def backtracking(subsets, currset, index):
            if index >= len(nums):
                subsets.append(currset.copy())
                return
            
            currset.append(nums[index])

            backtracking(subsets, currset, index + 1)
            currset.pop()
            backtracking(subsets, currset, index + 1)


        backtracking(subsets, currset, 0)
        return subsets
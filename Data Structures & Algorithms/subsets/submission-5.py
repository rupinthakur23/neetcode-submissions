class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        currList, resultList = [], []

        def backtracking(i):
            if i == len(nums):
                resultList.append(currList.copy())
                return
            
            currList.append(nums[i])
            backtracking(i + 1)
            currList.pop()
            backtracking(i + 1)



        backtracking(0)
        return resultList
        
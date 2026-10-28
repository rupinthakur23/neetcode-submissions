class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtracking(i):
            if i == len(nums):
                return [[]]
            
            perms = backtracking(i + 1)
            premsList = []

            for perm in perms:
                for j in range(len(perm) + 1):
                    permCopy = perm.copy()
                    permCopy.insert(j, nums[i])
                    premsList.append(permCopy)

            return premsList
        
        return backtracking(0)

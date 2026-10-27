class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtracking(i):
            if i == len(nums):
                return [[]]
            
            perms = backtracking(i + 1)
            resultPerms = []

            for p in perms:
                for c in range(len(p) + 1):
                    pCopy = p.copy()
                    pCopy.insert(c, nums[i])
                    resultPerms.append(pCopy)
            
            return resultPerms

        return backtracking(0)
        
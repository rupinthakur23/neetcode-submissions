class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        subset, currset = [], []

        def backtracking(total, index):
            if total == target:
                subset.append(currset.copy())
                return
            
            if total > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                currset.append(candidates[i])
                backtracking(total + candidates[i], i + 1)
                currset.pop()
        
        backtracking(0, 0)
        return subset
        
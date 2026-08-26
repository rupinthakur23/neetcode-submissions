class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result, subset = [], []

        def dfs(index, total):
            if total == target:
                result.append(subset.copy())
                return
            
            if index >=len(candidates) or total > target:
                return 
            
            for j in range(index, len(candidates)):
                if j > index and candidates[j] == candidates[j-1]:
                    continue
                subset.append(candidates[j])

                dfs(j + 1, total + candidates[j])
                subset.pop()
        

        dfs(0,0)
        return result

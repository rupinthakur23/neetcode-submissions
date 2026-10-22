class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        resultSet, currSet = [], []
        candidates.sort()

        def dfs(total, index):

            if total == target:
                resultSet.append(currSet.copy())
                return
            
            if total > target:
                return

            for j in range(index, len(candidates)):

                if j > index and candidates[j] == candidates[j-1]:
                            continue
                currSet.append(candidates[j])

                dfs(total + candidates[j], j + 1)

                currSet.pop()
        
        dfs(0, 0)
        return resultSet
        
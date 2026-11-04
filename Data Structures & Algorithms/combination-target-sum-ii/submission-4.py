class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        currList, resultList = [], []

        def backtracking(i, total):
            if total == target:
                resultList.append(currList.copy())
                return

            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                currList.append(candidates[j])
                backtracking(j + 1, total + candidates[j])
                currList.pop()


        backtracking(0, 0)
        return resultList
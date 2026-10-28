class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curList, resList = [], []

        def backtracking(i, total):
            if total == target:
                resList.append(curList.copy())
                return
            
            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                total += candidates[j]
                curList.append(candidates[j])
                backtracking(j + 1, total)

                total -= candidates[j]
                curList.pop()

        backtracking(0, 0)
        return resList
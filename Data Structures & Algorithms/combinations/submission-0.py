class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, subset = [], []

        def dfs(index):
            if len(subset) == k:
                result.append(subset.copy())
                return
            

            for i in range(index, n + 1):
                subset.append(i)
                dfs(i + 1)
                subset.pop()

        dfs(1)

        return result

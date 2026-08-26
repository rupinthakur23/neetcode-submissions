class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = defaultdict(int)

        for dr, ds in trust:
            trustMap[dr] -= 1
            trustMap[ds] += 1

        
        for i in range(1,n + 1):
            if trustMap[i] == n -1:
                return i

        return -1


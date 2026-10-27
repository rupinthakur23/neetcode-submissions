class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming, outcoming = defaultdict(int), defaultdict(int)

        for u, v in trust:
            incoming[u] +=1
            outcoming[v] +=1
        
        for i in range(1, n + 1):
            if (outcoming[i] - incoming[i]) == (n - 1):
                return i
        
        return -1
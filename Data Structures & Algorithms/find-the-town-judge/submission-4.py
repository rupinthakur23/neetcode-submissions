class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        judgeMap = defaultdict(int)

        for uv, uw in trust:
            judgeMap[uv] -=1
            judgeMap[uw] +=1
        
        for i in range(1,n + 1):
            if judgeMap[i] == (n -1):
                return i
        
        return -1

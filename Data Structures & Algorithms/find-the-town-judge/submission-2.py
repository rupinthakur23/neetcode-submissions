class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ajaencyList = defaultdict(list)
        outcome = defaultdict(int)

        for uv, uw in trust:
            ajaencyList[uv].append(uw)
        
        for i in range(1, n + 1):
            val = ajaencyList[i]
            if val:
                outcome[val[0]] +=1
                outcome[i] -=1
        for key, val in outcome.items():
            if val == n -1:
                return key
        
        return -1
        

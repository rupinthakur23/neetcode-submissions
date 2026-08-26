class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outcoming =  defaultdict(int)

        for dr, ds in trust:
            incoming[dr] +=1
            outcoming[ds] +=1
        

        for i in range(1, n +1):
            if incoming[i] == 0 and outcoming[i] == n -1:
                return i
        
        return -1
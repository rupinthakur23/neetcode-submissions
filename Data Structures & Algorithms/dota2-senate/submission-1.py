class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        D,R = deque(), deque()

        for i, val in enumerate(senate):
            if val == 'R':
                R.append(i)
            else:
                D.append(i)
        
        while D and R:

            DTurn = D.popleft()
            RTurn = R.popleft()

            if DTurn < RTurn:
                D.append(DTurn + len(senate))
            else:
                R.append(RTurn + len(senate))
        
        return "Radiant" if R else 'Dire'

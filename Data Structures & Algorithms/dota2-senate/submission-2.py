class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Dqueue = deque()
        Rqueue = deque()

        for i, val in enumerate(senate):
            if val == 'R':
                Rqueue.append(i)
            else:
                Dqueue.append(i)

        while Rqueue and Dqueue:
            rNode = Rqueue.popleft()
            dNode = Dqueue.popleft()

            if dNode > rNode:
                Rqueue.append(rNode + len(senate))
            else:
                Dqueue.append(dNode + len(senate))
        
        return "Radiant" if Rqueue else "Dire"
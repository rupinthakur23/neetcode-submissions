class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rqueue, Dqueue = deque(), deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                Rqueue.append(i)
            else:
                Dqueue.append(i)

        while Dqueue and Rqueue:
            Rsenate = Rqueue.popleft()
            Dsenate = Dqueue.popleft()

            if Rsenate > Dsenate:
                Dqueue.append(Dsenate + len(senate))
            else:
                Rqueue.append(Rsenate + len(senate))
        
        return 'Radiant' if Rqueue else 'Dire'
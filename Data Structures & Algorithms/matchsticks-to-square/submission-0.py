class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if (sum(matchsticks) % 4) != 0:
            return False
        
        sides = [0] * 4
        target = sum(matchsticks) /4
        matchsticks.sort(reverse = True)

        def backtracking(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for j in range(4):
                if sides[j] + matchsticks[i] > target:
                    continue
                
                sides[j] += matchsticks[i]

                if backtracking(i + 1):
                    return True
                
                sides[j] -= matchsticks[i]
            return False


        return backtracking(0)
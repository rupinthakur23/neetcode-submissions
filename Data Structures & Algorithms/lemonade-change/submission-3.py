class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount, tenCount = 0, 0

        for bill in bills:
            if bill == 5:
                fiveCount +=1
            elif bill == 10:
                fiveCount -=1
                tenCount +=1
            else:
                if tenCount:
                    fiveCount -=1
                    tenCount -=1
                else:
                    fiveCount -=3
            
            if fiveCount < 0:
                return False
        
        return True
        
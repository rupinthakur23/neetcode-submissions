class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveBills, tenBills = 0, 0

        for bill in bills:
            if bill == 5:
                fiveBills +=1
            elif bill == 10:
                tenBills +=1
                fiveBills -=1
            else:
                if tenBills:
                    tenBills -=1
                    fiveBills -=1
                else:
                    fiveBills -=3
            
            if fiveBills <0:
                return False
        return True

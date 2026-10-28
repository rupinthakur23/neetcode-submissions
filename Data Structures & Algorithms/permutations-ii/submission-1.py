class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permMap = {n:0 for n in nums}
        currList, result = [], []

        for n in nums:
            permMap[n] +=1
        
        def backtracking():
            if len(currList) == len(nums):
                result.append(currList.copy())
                return
            
            for n in permMap:
                if permMap[n] > 0:
                    currList.append(n)
                    permMap[n] -=1

                    backtracking()
                    currList.pop()
                    permMap[n] +=1
        
        
        backtracking()
        return result
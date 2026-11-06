class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        store = {}

        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        currList, resultList = [], []

        def backtracking(i):
            if i == len(nums):
                resultList.append(currList.copy())
                return
            
            for n in store:
                if store[n] > 0:
                    currList.append(n)
                    store[n] -=1

                    backtracking(i + 1)
                    currList.pop()
                    store[n] +=1


        backtracking(0)
        return resultList
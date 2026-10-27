class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1

        def backtracking():
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for i in count:
                if count[i] > 0:
                    curr.append(i)
                    count[i] -=1

                    backtracking()
                    curr.pop()
                    count[i] +=1

        backtracking()
        return res
        


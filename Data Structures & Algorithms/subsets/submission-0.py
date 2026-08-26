class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, subset):
            nonlocal result

            if index == len(nums):
                result.append(subset.copy())
                return
            
            sunset = subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            dfs(index + 1, subset)
        
        dfs(0,[])

        return result


        
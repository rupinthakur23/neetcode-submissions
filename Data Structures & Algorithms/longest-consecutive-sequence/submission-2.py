class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        result = 0

        for num in nums:
            if num - 1 in visited:
                continue
            
            length = 1

            while num + length in visited:
                length +=1
            result = max(result, length)
        
        return result
        
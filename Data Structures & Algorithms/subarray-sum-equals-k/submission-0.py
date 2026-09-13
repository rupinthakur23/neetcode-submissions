class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        prefix = 0
        result = 0

        for num in nums:
            prefix += num 
            diff = prefix - k

            if diff in hashMap:
                result += hashMap[diff]
            hashMap[prefix] = hashMap.get(prefix, 0) + 1
        
        return result
                
            

            


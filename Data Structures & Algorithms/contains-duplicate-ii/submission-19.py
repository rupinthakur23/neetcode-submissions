class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        uniques = set()

        for r in range(len(nums)):
            if (r - l) > k:
                uniques.remove(nums[l])
                l +=1
            
            if nums[r] in uniques:
                return True
        
            uniques.add(nums[r])
        return False

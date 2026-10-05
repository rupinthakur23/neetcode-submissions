class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        uniques = set()

        for r in range(len(nums)):
            if nums[r] not in uniques:
                uniques.add(nums[r])
            else:
                while nums[r] != nums[l]:
                    l +=1
                
                if (r - l) <= k:
                    return True
                l +=1
        return False

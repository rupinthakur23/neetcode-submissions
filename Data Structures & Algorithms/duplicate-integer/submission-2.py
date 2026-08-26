class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = set()

        for num in nums:
            if num in bucket:
                return True
            else:
                bucket.add(num)
        return False
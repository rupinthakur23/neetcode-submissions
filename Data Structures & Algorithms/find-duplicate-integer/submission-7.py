class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        start = nums[0]

        while start != slow:
            slow = nums[slow]
            start = nums[start]
        
        return start


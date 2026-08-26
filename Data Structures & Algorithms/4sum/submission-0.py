class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        start = 0

        while(start < len(nums) - 3):
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue
            first = start + 1
            while(first < len(nums) - 2):
                left, right = first + 1, len(nums) - 1
                if first > start + 1 and nums[first] == nums[first - 1]:
                    first +=1
                    continue
                while(left < right):
                    total = nums[start] + nums[first] + nums[left] + nums[right]

                    if total > target:
                        right -=1
                    elif total < target:
                        left += 1
                    else:
                        result.append([nums[start], nums[first], nums[left], nums[right]])
                        left +=1
                        right -=1

                        while ( left < right and nums[left] == nums[left - 1]):
                            left +=1
                first +=1
            start +=1
        return result
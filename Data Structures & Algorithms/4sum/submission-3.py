class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        quad = []

        def returnSum(left, right, target):
            while(left < right):
                total = nums[left] + nums[right] 
                if total > target:
                    right -=1
                elif total < target:
                    left +=1
                else:
                    result.append(quad + [nums[left], nums[right]])

                    left+=1
                    right -=1

                    while(left < right and nums[left] == nums[left -1]):
                        left+=1
            return

        def kSum(k, start, target):
            if k ==2:
                returnSum(start, len(nums) - 1, target)
                return
            for index in range(start,len(nums) - k + 1):
                if(index >start and nums[index] == nums[index - 1]):
                    continue
                quad.append(nums[index])
                kSum(k-1,index + 1, target - nums[index])
                quad.pop()

        kSum(4, 0, target)
        return result
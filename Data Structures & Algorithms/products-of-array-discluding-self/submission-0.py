class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix, postfix = [1] * len(nums), [1] * len(nums)
        prefixTotal, postfixTotal = 1,1

        for i in range(1, len(nums)):
            prefixTotal *= nums[i - 1]
            prefix[i] = prefixTotal

        for i in range(len(nums) - 2, -1, -1):
                postfixTotal *= nums[i + 1]
                postfix[i] = postfixTotal
        
        for i in range(0, len(nums)):
            result.append(prefix[i] * postfix[i])
        
        return result


        

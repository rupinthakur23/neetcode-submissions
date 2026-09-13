class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] +=1

            if len(count) <=2:
                continue
            
            newCount = defaultdict(int)

            for key, value in count.items():
                if value > 1:
                    newCount[key] = value -1
            
            count = newCount
        
        result = []

        for num in count:
            if nums.count(num) > (len(nums)//3):
                result.append(num)

        return result
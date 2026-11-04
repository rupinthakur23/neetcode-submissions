class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if (sum(nums) % k) != 0:
            return False
        target = sum(nums) // k
        nums.sort(reverse = True)
        visited = [False] * len(nums)

        def backtracking(i, total, k):
            if k == 0:
                return True
            
            if total == target:
                return backtracking(0, 0, k - 1)
            
            for j in range(i, len(nums)):
                if visited[j] or (total + nums[j]) > target:
                    continue
                visited[j] = True
                if backtracking(j + 1, total + nums[j], k):
                    return True
                visited[j] = False
                if total == 0:
                    break
            return False

        return backtracking(0, 0, k)
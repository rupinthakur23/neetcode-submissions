class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1

        while left < right:
            mid = left + (right - left)//2

            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        pivot = left
        
        left, right = 0, pivot - 1

        while left <=right:
            mid = left + (right - left)//2

            midNum = mountainArr.get(mid)
            if midNum > target:
                right = mid - 1
            elif midNum < target:
                left = mid + 1
            else:
                return mid

        left, right = pivot, mountainArr.length() - 1

        while left <=right:
            mid = left + (right - left)//2

            midNum = mountainArr.get(mid)
            if midNum > target:
                left = mid + 1
            elif midNum < target:
                right = mid - 1
            else:
                return mid
        
        return -1











class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1

        while left < right:
            mid = left + (right - left)//2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left

        left, right = 0, peak - 1

        while left <= right:
            mid = left + (right - left)//2

            if mountainArr.get(mid) < target:
                left = mid + 1
            elif mountainArr.get(mid) > target:
                right = mid - 1
            else:
                return mid
        

        left, right = peak, mountainArr.length() - 1

        while left <= right:
            mid = left + (right - left)//2

            if mountainArr.get(mid) < target:
                right = mid - 1
            elif mountainArr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        
        return -1



        
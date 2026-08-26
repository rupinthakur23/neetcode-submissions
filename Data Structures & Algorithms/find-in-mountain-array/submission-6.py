class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        left, right = 0, mountainArr.length() - 1

        while left < right:
            mid = left + ((right - left)//2)


            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                right = mid
            else:
                left = mid + 1
        
        peak = left
        print(peak)

        left, right = 0, peak - 1

        while left <= right:
            mid = left + ((right - left)//2)

            midValue = mountainArr.get(mid)

            if midValue > target:
                right = mid - 1
            elif midValue < target:
                left = mid + 1
            else:
                return mid

        left, right = peak, mountainArr.length() - 1

        while left <= right:
            mid = left + ((right - left)//2)

            midValue = mountainArr.get(mid)

            if midValue > target:
                left = mid + 1
            elif midValue < target:
                right = mid - 1
            else:
                return mid

        return -1
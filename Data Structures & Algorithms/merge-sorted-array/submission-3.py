class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last, left, right = len(nums1) - 1, m -1, n -1 

        while(right >= 0):
            if( left>=0 and nums1[left] >= nums2[right]):
                nums1[last] = nums1[left]
                left-= 1
            else:
                nums1[last] = nums2[right]
                right-= 1
            last -= 1

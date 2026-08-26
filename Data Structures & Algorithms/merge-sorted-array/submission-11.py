class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right, pointer = m - 1, n -1, m + n -1

        while left >=0 and right >=0:
            if nums1[left] > nums2[right]:
                nums1[pointer] = nums1[left] 
                pointer -=1
                left -=1
            else:
                nums1[pointer] = nums2[right] 
                pointer -=1
                right -=1
        
        
        while left >= 0:
            nums1[pointer] = nums1[left] 
            pointer -=1
            left -=1
        
        while right >= 0:
            nums1[pointer] = nums2[right] 
            pointer -=1
            right -=1



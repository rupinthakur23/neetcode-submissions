class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, l, m, r):
            numsLeft = arr[l: m + 1]
            numsRight = arr[m + 1: r + 1]
            i, j, k = 0,0, l

            while i < len(numsLeft) and j < len(numsRight):
                if numsLeft[i] >= numsRight[j]:
                    arr[k] = numsRight[j]
                    j +=1
                else:
                    arr[k] = numsLeft[i]
                    i +=1
                k +=1   

            while i < len(numsLeft):
                arr[k] = numsLeft[i]
                i +=1
                k +=1

            while j < len(numsRight):
                arr[k] = numsRight[j]
                j +=1
                k +=1

        def mergeSort(arr, l, r):
            if l >=r:
                return
            m = (l + r)//2
            mergeSort(arr,l, m)
            mergeSort(arr, m + 1, r)
            merge(arr,l,m,r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums
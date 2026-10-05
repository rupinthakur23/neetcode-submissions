class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, result, prev, r = 0, 1, '', 1

        while r < len(arr):
            if arr[r] > arr[r - 1] and prev != '>':
                result = max(result, r - l + 1)
                prev = '>'
                r +=1
            elif arr[r] < arr[r - 1] and prev != '<':
                result = max(result, r - l + 1)
                prev = '<'
                r +=1
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ''
        return result

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n):
            j = i + 1
            while(j< n  and temperatures[i] >= temperatures[j] ):
                j = j+ 1;
            if ( j == n ):
                res[i] = 0
            else:
                res[i] = j - i
        return res

        
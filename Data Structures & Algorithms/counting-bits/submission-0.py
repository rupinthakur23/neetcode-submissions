class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            current = i
            oneTotal = 0

            while current > 0:
                current = current & (current -1)
                oneTotal += 1
            result[i] = oneTotal
        return result
        
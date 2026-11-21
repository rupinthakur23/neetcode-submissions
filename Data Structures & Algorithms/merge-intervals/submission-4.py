class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda t: t[0])
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = result[-1]

            if intervals[i][0] > prev[1]:
                result.append(intervals[i])
            else:
                result.pop()
                result.append([min(intervals[i][0], prev[0]), max(intervals[i][1], prev[1])])
        return result
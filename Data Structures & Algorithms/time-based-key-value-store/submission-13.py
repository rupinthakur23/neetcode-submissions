class TimeMap:

    def __init__(self):
        self.timeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap.get(key, [])
        result = float('-inf')
        if not values:
            return ""
        
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if values[mid][1] <= timestamp:
                result = max(result, mid)
                left = mid + 1
            else:
                right = mid -1
        
        return values[result][0] if result != float('-inf') else ''
        


        

        

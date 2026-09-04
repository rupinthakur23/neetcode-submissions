class TimeMap:

    def __init__(self):
        self.timeStamp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStamp:
            self.timeStamp[key] = []
        self.timeStamp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ''
        values = self.timeStamp.get(key, [])
        
        left, right = 0, len(values) - 1

        while left <= right:
            mid = left + (right - left)//2

            if values[mid][1] > timestamp:
                right = mid - 1
            else:
                result = values[mid][0]
                left = mid + 1
        
        return result
        

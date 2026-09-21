class CountSquares:

    def __init__(self):
        self.pointMap = defaultdict(int)
        self.pts = []
        
    def add(self, point: List[int]) -> None:
        self.pointMap[tuple(point)] += 1
        self.pts.append(point)
        
    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point

        for x, y in self.pts:
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue
            
            result += self.pointMap[(px, y)] * self.pointMap[(x, py)]
        return result
            
        

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carMap = {(position, speed) for position, speed in zip(position, speed)}
        stack = []

        for position, speed in sorted(carMap)[::-1]:
            time = (target - position)/speed
            stack.append(time)

            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)



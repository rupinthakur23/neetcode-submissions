class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carMap = [[pos,spe] for pos, spe in zip(position, speed)]
        stack = []

        for pos, speed in sorted(carMap, reverse = True):
            time = (target - pos) / speed
            stack.append(time)

            while stack and len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

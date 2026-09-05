class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carData = [[position, speed] for position, speed in zip(position, speed)]
        stack = []

        for pos, spe in sorted(carData)[::-1]:
            time = (target - pos)/spe
            stack.append(time)

            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        

        return len(stack)





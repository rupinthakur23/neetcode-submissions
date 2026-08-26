class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            survive = True

            while stack and stack[-1] > 0 and asteroid <0:
                if stack[-1] > abs(asteroid):
                    survive = False
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                else:
                    stack.pop()
                    survive = False
                    break

            if survive:
                stack.append(asteroid)
        return stack
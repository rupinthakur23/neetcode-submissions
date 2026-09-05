class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            survive = True
            while stack and asteroid < 0 and stack[-1] >0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) < stack[-1]:
                    survive = False
                    break
                else:
                    stack.pop()
                    survive = False
                    break

            if survive:
                stack.append(asteroid)
        
        return stack
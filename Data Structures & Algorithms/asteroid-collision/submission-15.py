class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            asteroidSurvive = True
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) < stack[-1]:
                    asteroidSurvive = False
                    break
                else:
                    stack.pop()
                    asteroidSurvive = False
                    break
            if asteroidSurvive:
                stack.append(asteroid)
        
        return stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            survived = True

            while stack and stack[-1] >0 and asteroid < 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] > abs(asteroid):
                    survived = False
                    break
                else:
                    stack.pop()
                    survived = False
                    break
            
            if survived:
                stack.append(asteroid)
        
        return stack

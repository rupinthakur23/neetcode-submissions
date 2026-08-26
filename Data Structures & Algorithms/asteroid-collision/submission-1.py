class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for index, value in enumerate(asteroids):
            if not stack:
                stack.append(value)
            else:
                if value > 0:
                    stack.append(value)
                else:
                    while(stack and stack[-1] > 0):
                        if(abs(value) > stack[-1]):
                            stack.pop()
                            continue
                        elif(abs(value) == stack[-1]):
                            stack.pop()
                        break
                    else:
                        stack.append(value)
        return stack

                            



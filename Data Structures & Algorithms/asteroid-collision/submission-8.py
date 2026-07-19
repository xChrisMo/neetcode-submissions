class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [asteroid, asteroid, asteroid, asteroid, asteroid, asteroid]
        
        # if positive, we add
        # if negative, we look at previous if positive, if it is, do a smash of both
        # if negative, if nothing prioir, negative
        # if negative, while prior is less, stack.pop(), add negative! 

        stack = []

        for i, ast in enumerate(asteroids):
            if ast > 0:
                # positive, moving right, add!
                # positivce would not have met a prior negative as they move in different directions
                stack.append(ast)

            else:
                
                # while stack[-1] > 0
                # while we have our stakc and the last seen is moving right.
                while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                    # if equal, remove both, continue 
                    stack.pop()

                    # prev greater than our negative ast:
                if stack and stack[-1] == abs(ast):
                        # break out of while loop
                    stack.pop()

                    # if abs(our current asteroid) is greater than it,
                    # elif stack[-1] < abs(ast):
                elif not stack or stack[-1] < 0:
                    stack.append(ast)

        return stack
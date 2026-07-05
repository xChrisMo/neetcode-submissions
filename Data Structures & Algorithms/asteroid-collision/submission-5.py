class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # [2, 4, -4, -1]

        # 1. if the one on the left is moving right AND the one on the right is moving left, 
        # they collide

        # 2. z
        stack = []

        for char in asteroids:
            if not stack: 
                stack.append(char)

            else:
                while stack and stack[-1] > 0 and char < 0:
                    diff = stack[-1] + char

                    if diff < 0: 
                        # left asteroid was bigger
                        stack.pop()
                    
                    elif diff > 0:
                        # collision is positive, [-1] > asteroid
                        char = 0

                    else:
                        # same value 
                        char = 0
                        stack.pop()

                if char:
                    print(f"char is {char}")
                    stack.append(char)


        return stack
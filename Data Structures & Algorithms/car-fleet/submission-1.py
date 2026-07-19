class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position, speed
        # [4,2], [1,2], [0,1], [7,1]
        # [[7,1], [4, 2], [1,2], [0,1]]

        arr = [[p, s] for p, s in zip(position, speed)]

        arr.sort(reverse=True)
        stack = []

        for p, s in arr:
            stack.append((target - p) / s)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()


        return len(stack)
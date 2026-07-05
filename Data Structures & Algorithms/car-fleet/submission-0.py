class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n 
        # position = [x, x, x]
        # speed =    [x, x, x]

        # 4:(2) - 6,8,10
        # 1:(2) - 3,5,7,9,10
        # 0:(1) - 1,2,3,4,5,6,7,8,9,10
        # 7:(1) - 8,9,10
        
        stack = []
        arr = [(p, s) for p, s in zip(position, speed)]
        arr.sort(reverse=True)

        for p, s in arr:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        
        # arr.sort(reverse=True)
            
        # for position, speed in arr:
        #     print(f'Position is {position}, with v == {speed}')
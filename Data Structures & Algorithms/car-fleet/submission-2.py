class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        a car will form a fleet when the time to get there is less than or equal to its next counter parts time 
        target=10
position=[4,1,0,7]
speed=[2,2,1,1]
stack [3 4.5]
        '''

        stack=[]
        for pos,speed in sorted(zip(position,speed))[::-1]:
            time=(target-pos)/speed
            stack.append(time)
            while len(stack)>=2 and  stack[-1]<=stack[-2]:
                stack.pop()
        print(len(stack))
        return len(stack)
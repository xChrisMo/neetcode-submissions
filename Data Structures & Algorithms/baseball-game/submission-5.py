class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # starts at empty, set, stack, dictionary, list
        
        # if '+', score[-1] + score[-2]
        # if 'D', add score[-1] * 2
        # if 'C', remove last score
        # if int, add record 

        # return sum()
        
        # |   |
        # |   |
        # | 10  |
        # |_5__|

        # ["C"]
        # ops = ["1","2","+","C","5","D"]

        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
        
            elif op == 'D':
                stack.append(stack[-1] * 2)
        
            elif op == 'C':
                stack.pop()

            else:
                stack.append(int(op))


        return sum(stack)
class Solution:
    def maxDepth(self, s: str) -> int:
        # max_n = 0
        # cur_n = 0

        # for char in s:
        #     if char == '(':
        #         cur_n += 1

        #         max_n = max(max_n, cur_n)
            
        #     elif char == ')':
        #         cur_n -= 1 


        # return max_n
        
        stack = []
        max_n = 0

        for char in s:
            if char == '(':
                stack.append(char)
                max_n = max(max_n, len(stack))
            
            elif char == ')':
                stack.pop()


        return max_n
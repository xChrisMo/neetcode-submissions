class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []

        # we need to have an out
        # we need to someway incrementally open and close a current_stack

        def subset(opened_count, closed_count):
            # base condition
            if opened_count == closed_count == n:
                out.append(''.join(stack))
                return 

            # we need to somehow include the openeing 

            if opened_count < n:
                stack.append('(')
                subset(opened_count + 1, closed_count)
                stack.pop()

            # i need to count the closed too, 
            # while closed < open
            if closed_count < opened_count:
                stack.append(')')
                subset(opened_count, closed_count + 1)
                stack.pop()

        subset(0, 0)
        return out
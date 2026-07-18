class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # C -> pop()
        # D -> stack.append(stack[-1] * stack[-2])
        # '+' -> stack.append(stack[-1] + stack[-2])

        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])

            elif op == 'C':
                stack = stack[:-1]

            elif op == 'D':
                stack.append(stack[-1] * 2)

            else:
                stack.append(int(op))


        return sum(stack)
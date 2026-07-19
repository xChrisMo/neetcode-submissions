class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == '+':
                first = stack.pop()
                second = stack.pop()

                stack.append(first + second)


            elif tok == '*':
                first = stack.pop()
                second = stack.pop()

                stack.append(first * second)
                

            elif tok == '/':
                first = stack.pop()
                second = stack.pop()

                stack.append(int(float(second) / first))
                
            elif tok == '-':
                first = stack.pop()
                second = stack.pop()

                stack.append(second - first)
                
            else:
                stack.append(int(tok))

        print(stack)

        return stack[-1]
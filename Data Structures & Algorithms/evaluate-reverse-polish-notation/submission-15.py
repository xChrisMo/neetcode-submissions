class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if +, pop last 2, add them togeterh, append to stack
        #if *, pop last 2, multiply them together, append to stack
        #if -, pop last 2, subtract first from second, append to stack
        #if /, float(b)/a

        stack = []

        for token in tokens:
            if token == '*':
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(first_ele * second_ele)

            elif token == '+':
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(first_ele + second_ele)

            elif token == '-':
                first_ele = stack.pop()
                second_ele = stack.pop()
                stack.append(second_ele - first_ele)

            elif token == '/':
                first_ele = stack.pop()
                second_ele = stack.pop()

                stack.append(int(float(second_ele) / first_ele))

            else:
                stack.append(int(token))
        
        print(stack)
        return int(stack[0])
        #never empty
        #always an answer
        #
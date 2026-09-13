class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for ele in tokens:
            if ele=="+":
                a=stack.pop()
                b=stack.pop()
                stack.append(a+b)
            elif ele=="*":
                stack.append(stack.pop()*stack.pop())
            elif ele=="-":
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif ele=="/":
                a=stack.pop()
                b=stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(ele))
        print(stack)
        return stack[0]
                
            

class Solution:
    def isValid(self, s: str) -> bool:
        # if opening, add to stack
        # if closing, check if last element is closing of opening

        dict_stack = {']':'[', '}':'{', ')':'('}
        stack = []

        for char in s:
            if char not in dict_stack:
                stack.append(char)

            else:
                if not stack or stack[-1] != dict_stack[char]:
                    return False

                else:
                    stack.pop()
        
        return True if not stack else False
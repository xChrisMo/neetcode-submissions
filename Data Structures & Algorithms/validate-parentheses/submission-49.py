class Solution:
    def isValid(self, s: str) -> bool:
        # we store '], ), }'sas keys really
        # else store others in a stack

        closed_dict = {'}':'{', ']':'[', ')':'('}
        stack = []


        for char in s:
            if char not in closed_dict:
                stack.append(char)

            else:
                if stack and stack[-1] == closed_dict[char]:
                    stack.pop()
                    continue

                else:
                    return False

        
        return len(stack) == 0

        # stack = '([{
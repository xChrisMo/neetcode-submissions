class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        print(path)

        stack = []
        for char in path:
            if char == '..':
                if len(stack) >= 1:
                    stack.pop()
                else:
                    continue
                
            elif char == '.':
                continue
                
            elif char != '':
                stack.append(char)
                
                

        return '/' + ('/').join(stack)
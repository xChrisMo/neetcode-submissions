class Solution:
    def simplifyPath(self, path: str) -> str:
        # ['/']

        # '.' -> current
        # '..' -> back!
        # '//' or '///' -> '/'
        # else '...' or '....' -> valid files

        stack = []
        path = path.split('/')

        # if char == '': continue
        # elif char == '..': if stack, pop()
        # elif char == '.': continue
        # apppend '/' after every new char.
        # elif char == '...': append
        # if out[-1] == '/', pop()!


        #['/', '_home', '/', 'a', '/', ]
        print(path)

        # ['', 'neetcode', 'practice', '', '...', '', '', '..', 'courses']
        # ['', '..', '', '']
        # ['', '..', '', '_home', 'a', 'b', '..', '', '', '']


        #['/', 'neetcode', '/', 'practice', '/', 'courses']

        for char in path:
            # if char == '': continue
            if char == '' or char == '.':
                continue
                                    
            # elif char == '..': if stack, pop()
            elif char == '..':
                if stack:
                    stack.pop() # remove actual char

            # elif char == '...': append
            # apppend '/' after every new char.
            else:
                stack.append(char)


        # if out[-1] == '/', pop()!
        return '/' + '/'.join(stack)
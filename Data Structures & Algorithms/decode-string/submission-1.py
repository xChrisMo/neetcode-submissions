class Solution:
    def decodeString(self, s: str) -> str:
        # if s != ']': stack.append(char)

        # 2, [, a, 3

        #else:
            # while stack[-1] != '[':

            #   FOR LETTERS
            #   word = ''
            #   while not stack[-1].is_digit():
            #       stack.pop() += word
            # stack.pop() # remove stray '['

        #   FOR INTEGERS
        #   val = 0
        #   while stack and stack[-1].is_digit():
        #       val = stack.pop() + val

        #   stack.append(word * int(val))

        #return ''.join(stack)

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)

            else:
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word

                # now char == '['
                stack.pop()

                val = ''
                while stack and stack[-1].isdigit():
                    val = stack.pop() + val

                stack.append(word * int(val))

        return ''.join(stack)
class Solution:
    def decodeString(self, s: str) -> str:
        # while it is not a ']', add to stack
        # if ']', while stack[-1] is not '[', build the word!
        # no2 it is '[', from there, while isalnum, 

        #[2, [, a, 3, [
        # while not '[', pop build word
        # word = 'b' 
        # now it is '['
        # pop, removes '['
        # while isalnum(), pop, build multiplier
        # stack.append(multiplier * word)

        stack = []

        for char in s:
            if char != ']':
                stack.append(char)

            else:
                word = ''
                while stack[-1] != '[':
                    word = stack.pop() + word

                # to remove the '['
                stack.pop()

                # 25

                # val = 2
                # base = 10
                # 5 + 20

                # build num
                base = 1
                out = 0
                while stack and stack[-1].isdigit():
                    val = stack.pop()
                    out += int(val) * base
                    base *= 10

                stack.append(out * word)
                
        return ''.join(stack)


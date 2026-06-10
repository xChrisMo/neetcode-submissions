class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #stack
        #if char == stack[-1] character, stack[-1][count] += 1, else stack.append(char)[1]
        # if stack[-1][count] == k: stack.pop()
        #''.join([ele*count for ele, count in stack])
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1

            else:
                stack.append([char, 1])

            if stack[-1][1] == k:
                        stack.pop()

        return ''.join([char * count for char, count in stack])
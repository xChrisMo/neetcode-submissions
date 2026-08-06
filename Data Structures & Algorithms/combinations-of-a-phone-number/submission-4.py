class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        out = []
        curset = []
        n = len(digits)
        if digits == "":
            return out

        def dfs(i):
            if i == len(digits):
                out.append(''.join(curset))
                return 

            for char in num_to_letters[digits[i]]:
                curset.append(char)
                dfs(i + 1)
                curset.pop()


        dfs(0)
        return out
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
        subset = []

        # edge case
        if digits == '':
            return []

        def dfs(i, curStr):
            # base case
            if len(curStr) == len(digits):
                out.append(curStr)
                return 

            # for each letter in digits, check all its possible usesss
            for c in num_to_letters[digits[i]]:
                dfs(i + 1, curStr + c)
                

        dfs(0, '')
        return out
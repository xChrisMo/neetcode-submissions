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
        
        if digits == '':
            return out

        def dfs(i, curSet):
            # base condition, we get possible combo for digits
            if i == len(digits):
                out.append(''.join(curSet[:]))
                return 

            for j in num_to_letters[digits[i]]:
                curSet.append(j)
                dfs(i + 1, curSet)
                curSet.pop()

        dfs(0, [])
        return out
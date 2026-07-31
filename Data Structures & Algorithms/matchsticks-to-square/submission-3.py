class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0: return False

        # else, sort, largest to smallest
        
        # then try see if it fits
        # if it fits means it is equal to target, continue recursion from there...
        # if it exceeds target at any point, return False
        # if it is perfectly target, recurse
        # if it is less, recurse moree
        target = total / 4
        matchsticks.sort(reverse=True)
        self.sides = [0] * 4

        def dfs(i):
            # base case, we used all matchsticks
            if i == len(matchsticks):
                return True

            for j in range(4):
                if self.sides[j] + matchsticks[i] <= target:
                    self.sides[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    # backtrack
                    self.sides[j] -= matchsticks[i]
                # if self.sides[j] == 0:
                #     break
            return False

        return dfs(0)

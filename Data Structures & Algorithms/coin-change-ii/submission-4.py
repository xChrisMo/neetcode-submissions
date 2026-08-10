class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        cache = {}
        def dfs(i, cur):
            if (i, cur) in cache:
                return cache[(i, cur)]

            if i >= n:
                cache[(i, cur)] = 0
                return cache[(i, cur)]

            if cur > amount:
                cache[(i, cur)] = 0
                return cache[(i, cur)]

            if cur == amount:
                cache[(i, cur)] = 1
                return cache[(i, cur)]

            cache[(i, cur)] = dfs(i + 1, cur) + dfs(i, cur + coins[i])
            return cache[(i, cur)]
            
        return dfs(0, 0)
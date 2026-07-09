class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # one obvious.base case  
        # it cant be a square if it isnt even a factor of 4
        
        if sum(matchsticks) % 4 != 0: return False

        # so now we have to make an array of size 4, 
        # where each element / subarray sums up to the side

        length = sum(matchsticks) // 4

        # sorting from largest to smallest lets us know if 1 element is larger than side, 
        # if it is greater, return False already
        out = []
        matchsticks.sort(reverse=True)
        sides = [0] * 4 

        def subset(i):
            # base condition
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if subset(i + 1) == True:
                        return True
                    sides[j] -= matchsticks[i]
            return False

        return subset(0)

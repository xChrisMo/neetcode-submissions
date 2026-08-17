class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #[left, right]
        # 

        # can only pick 2 indexes
        # return the window of those two indexes 

        # use a set to store only two indexes
        # if the length of set > 2, keep removing from the window from l. 
        # remove the element at l too from the stack!
        # keep checking the max r - l + 1
        # so the check would have to be the first thing in our for loop

        l = 0
        seen = dict()
        max_r = 0

        for r in range(len(fruits)):
            seen[fruits[r]] = seen.get(fruits[r], 0) + 1
                
            while len(seen) > 2:
                seen[fruits[l]] -= 1
                if seen[fruits[l]] == 0:
                    del seen[fruits[l]]
                l += 1


            max_r = max(max_r, r - l + 1)

        return max_r
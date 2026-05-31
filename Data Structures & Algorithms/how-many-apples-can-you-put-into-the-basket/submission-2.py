class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        running_sum = 0
        pick = 0

        for w in weight:
            running_sum += w
            
            if running_sum > 5000:
                break 

            pick += 1

        return pick
